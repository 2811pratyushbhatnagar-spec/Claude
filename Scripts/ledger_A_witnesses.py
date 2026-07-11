# Ledger A — finite-model arbiter harness (v0.1, FROZEN with ledger_A_math_v0.1_frozen.md)
# Register: internal computation. Not refereed theorems. No interpretation layer (Ledger C empty).
# Model = (I, C, dom, cod, comp: partial dict, inv: set of pairs, S, at, en, step)

from itertools import product

def identities(M):
    I,C,dom,cod,comp,inv,S,at,en,step = M
    ids={}
    for i in I:
        for e in C:
            if dom[e]==i==cod[e] \
               and all(comp.get((e,c))==c for c in C if dom[c]==i) \
               and all(comp.get((c,e))==c for c in C if cod[c]==i):
                ids[i]=e; break
    return ids

def stepr(M,c):
    return {(s,t) for (cc,s,t) in M[9] if cc==c}

def bisim(M):
    I,C,dom,cod,comp,inv,S,at,en,step = M
    # partition refinement: same interface, same enabled set, matching successors
    part={s:(at[s],frozenset(c for c in C if (c,s) in en)) for s in S}
    for _ in range(len(S)):
        newpart={}
        for s in S:
            sig=[]
            for c in C:
                succ=frozenset(part[t] for (cc,ss,t) in step if cc==c and ss==s)
                sig.append(succ)
            newpart[s]=(part[s],tuple(sig))
        if newpart==part: break
        part=newpart
    return lambda x,y: part[x]==part[y]

def check(M, A3mode='strict', Fmode='eq', EImode='strong'):
    I,C,dom,cod,comp,inv,S,at,en,step = M
    r={}
    r['A1']=all(cod[a]==dom[b] and dom[c]==dom[a] and cod[c]==cod[b] for (a,b),c in comp.items())
    ok=True
    for (a,b),ab in comp.items():
        for c in C:
            if (b,c) in comp and (ab,c) in comp and (a,comp[(b,c)]) in comp:
                if comp[(ab,c)]!=comp[(a,comp[(b,c)])]: ok=False
    r['A2']=ok
    ids=identities(M)
    ok=len(ids)==len(I)
    if ok:
        for i,e in ids.items():
            diag={(s,s) for s in S if at[s]==i}
            se=stepr(M,e)
            if A3mode=='strict' and se!=diag: ok=False
            if A3mode=='loose' and not diag<=se: ok=False
            if not all((e,s) in en for s in S if at[s]==i): ok=False
    r['A3']=ok
    if ids and len(ids)==len(I):
        r['A4']=all(any((c,d) in inv and comp.get((c,d))==ids[dom[c]] and comp.get((d,c))==ids[cod[c]]
                        for d in C) for c in C)
    else:
        r['A4']=all(any((c,d) in inv for d in C) for c in C) and bool(inv)
    r['A5']=all(((c,s) in en) and at[s]==dom[c] and at[t]==cod[c] for (c,s,t) in step)
    ok=True
    for (a,b),c3 in comp.items():
        lhs=stepr(M,c3)
        rhs={(s,t) for (s,m) in stepr(M,a) for (m2,t) in stepr(M,b) if m2==m}
        if Fmode=='eq' and lhs!=rhs: ok=False
        if Fmode=='sub' and not lhs<=rhs: ok=False
        if Fmode=='sup' and not lhs>=rhs: ok=False
    r['F']=ok
    ok=True; bs=bisim(M)
    for (c,d) in inv:
        sc=stepr(M,c); sd=stepr(M,d); conv={(t,s) for (s,t) in sc}
        if EImode=='strong' and sd!=conv: ok=False
        if EImode=='w1' and not conv<=sd: ok=False
        if EImode=='w2' and not sd<=conv: ok=False
        if EImode=='bisim':
            for (s,t) in sc:
                if not any(t2==t and bs(s2,s) for (t2,s2) in sd): ok=False
    r['EI']=ok
    reach={(i,i) for i in I}
    for _ in I: reach |= {(dom[c],cod[c]) for c in C} | {(x,z) for (x,y) in reach for (y2,z) in reach if y==y2}
    r['T']=all((i,j) in reach for i in I for j in I)
    sre={(s,s) for s in S}
    for _ in S: sre |= {(s,t) for (c,s,t) in step} | {(x,z) for (x,y) in sre for (y2,z) in sre if y==y2}
    r['R']=all((t,s) in sre for (c,s,t) in step)
    return r

# ---------- Witness series ----------
W={}
# W1: maximal point — transitive groupoid, coherent effects
I=[0,1]; C=['e0','e1','f','g']
dom={'e0':0,'e1':1,'f':0,'g':1}; cod={'e0':0,'e1':1,'f':1,'g':0}
comp={('e0','e0'):'e0',('e1','e1'):'e1',('e0','f'):'f',('f','e1'):'f',
      ('e1','g'):'g',('g','e0'):'g',('f','g'):'e0',('g','f'):'e1'}
inv={('f','g'),('g','f'),('e0','e0'),('e1','e1')}
S=['a','b']; at={'a':0,'b':1}
en={('e0','a'),('e1','b'),('f','a'),('g','b')}
step={('e0','a','a'),('e1','b','b'),('f','a','b'),('g','b','a')}
W['W1']=(I,C,dom,cod,comp,inv,S,at,en,step)

# W2p: not-A4 only (f,g both present, mutually returning, but NOT inverses; T,R hold)
comp2={('e0','e0'):'e0',('e1','e1'):'e1',('e0','f'):'f',('f','e1'):'f',('e1','g'):'g',('g','e0'):'g'}
inv2={('e0','e0'),('e1','e1')}
W['W2p']=(I,C,dom,cod,comp2,inv2,S,at,en,step)

# W3: not-F and not-EI (algebra invertible, effects incoherent)
S3=['a','a2','b']; at3={'a':0,'a2':0,'b':1}
en3={('e0','a'),('e0','a2'),('e1','b'),('f','a'),('g','b')}
step3={('e0','a','a'),('e0','a2','a2'),('e1','b','b'),('f','a','b'),('g','b','a2')}
W['W3']=(I,C,dom,cod,comp,inv,S3,at3,en3,step3)

# W4: nondeterministic step (relation, not function) — core-consistent
C4=['e0','e1','h']; dom4={'e0':0,'e1':1,'h':0}; cod4={'e0':0,'e1':1,'h':1}
comp4={('e0','e0'):'e0',('e1','e1'):'e1',('e0','h'):'h',('h','e1'):'h'}
S4=['a','b1','b2']; at4={'a':0,'b1':1,'b2':1}
en4={('e0','a'),('e1','b1'),('e1','b2'),('h','a')}
step4={('e0','a','a'),('e1','b1','b1'),('e1','b2','b2'),('h','a','b1'),('h','a','b2')}
W['W4']=(I,C4,dom4,cod4,comp4,set(),S4,at4,en4,step4)

# W6: bisim-undo only (return to an equivalent copy, not the same state)
S6=['a','ap','b']; at6={'a':0,'ap':0,'b':1}
en6={('e0','a'),('e0','ap'),('e1','b'),('f','a'),('f','ap'),('g','b')}
step6={('e0','a','a'),('e0','ap','ap'),('e1','b','b'),('f','a','b'),('f','ap','b'),('g','b','ap')}
W['W6']=(I,C,dom,cod,comp,inv,S6,at6,en6,step6)

# W7a: F-sub pathology — composite licenses nothing (decorative compose)
I7=[0,1,2]; C7=['x0','x1','x2','f','k','m']
dom7={'x0':0,'x1':1,'x2':2,'f':0,'k':1,'m':0}; cod7={'x0':0,'x1':1,'x2':2,'f':1,'k':2,'m':2}
comp7={('x0','x0'):'x0',('x1','x1'):'x1',('x2','x2'):'x2',
       ('x0','f'):'f',('f','x1'):'f',('x1','k'):'k',('k','x2'):'k',
       ('x0','m'):'m',('m','x2'):'m',('f','k'):'m'}
S7=['a','b','c']; at7={'a':0,'b':1,'c':2}
en7={('x0','a'),('x1','b'),('x2','c'),('f','a'),('k','b'),('m','a')}
step7a={('x0','a','a'),('x1','b','b'),('x2','c','c'),('f','a','b'),('k','b','c')}  # m: no step
W['W7a']=(I7,C7,dom7,cod7,comp7,set(),S7,at7,en7,step7a)
# W7b: F-sup pathology — composite invents a transition its parts cannot do
step7b=step7a | {('m','a','c'),('m','a','c')} # legit part
S7b=['a','a2','b','c']; at7b={'a':0,'a2':0,'b':1,'c':2}
en7b=en7 | {('x0','a2'),('m','a2')}
step7bb={('x0','a','a'),('x0','a2','a2'),('x1','b','b'),('x2','c','c'),
         ('f','a','b'),('k','b','c'),('m','a','c'),('m','a2','c')}  # (a2,c) is magic
W['W7b']=(I7,C7,dom7,cod7,comp7,set(),S7b,at7b,en7b,step7bb)

# W8: idle availability — enabled with no licensed effect (inexpressible if en:=dom(step))
en8=en | {('f','a')}
step8={('e0','a','a'),('e1','b','b'),('g','b','a')}  # f enabled at a, no step
W['W8']=(I,C,dom,cod,comp2,inv2,S,at,en8,step8)

# W9: not-A3 only (no identities; comp empty; bare inv relation)
C9=['k']; dom9={'k':0}; cod9={'k':0}
S9=['a','a2']; at9={'a':0,'a2':0}
W['W9']=([0],C9,dom9,cod9,{}, {('k','k')}, S9, at9,
         {('k','a'),('k','a2')}, {('k','a','a2'),('k','a2','a')})

# W10: not-F only (EI holds: g exactly undoes f; but composite e0 acts on a2 which f;g misses)
step10={('e0','a','a'),('e0','a2','a2'),('e1','b','b'),('f','a','b'),('g','b','a')}
en10={('e0','a'),('e0','a2'),('e1','b'),('f','a'),('g','b')}
W['W10']=(I,C,dom,cod,comp,inv,S3,at3,en10,step10)

# W11: loose-A3 + F-eq + A4 hold, EI-strong FAILS -> strict A3 is NECESSARY for the derivation
S11=['a','a2','b','b2']; at11={'a':0,'a2':0,'b':1,'b2':1}
en11={('e0','a'),('e0','a2'),('e1','b'),('e1','b2'),('f','a'),('f','a2'),('g','b'),('g','b2')}
step11={('e0','a','a'),('e0','a2','a2'),('e0','a','a2'),
        ('e1','b','b'),('e1','b2','b2'),('e1','b','b2'),
        ('f','a','b'),('f','a','b2'),('f','a2','b2'),
        ('g','b','a'),('g','b','a2'),('g','b2','a2')}
W['W11']=(I,C,dom,cod,comp,inv,S11,at11,en11,step11)

# W12: not-T only (two disconnected groupoid components)
I12=[0,1,2,3]; C12=['e0','e1','f','g','e2','e3','p','q']
dom12={'e0':0,'e1':1,'f':0,'g':1,'e2':2,'e3':3,'p':2,'q':3}
cod12={'e0':0,'e1':1,'f':1,'g':0,'e2':2,'e3':3,'p':3,'q':2}
comp12=dict(comp); comp12.update({('e2','e2'):'e2',('e3','e3'):'e3',('e2','p'):'p',('p','e3'):'p',
       ('e3','q'):'q',('q','e2'):'q',('p','q'):'e2',('q','p'):'e3'})
inv12=inv|{('p','q'),('q','p'),('e2','e2'),('e3','e3')}
S12=['a','b','c','d']; at12={'a':0,'b':1,'c':2,'d':3}
en12={('e0','a'),('e1','b'),('f','a'),('g','b'),('e2','c'),('e3','d'),('p','c'),('q','d')}
step12={('e0','a','a'),('e1','b','b'),('f','a','b'),('g','b','a'),
        ('e2','c','c'),('e3','d','d'),('p','c','d'),('q','d','c')}
W['W12']=(I12,C12,dom12,cod12,comp12,inv12,S12,at12,en12,step12)

# ---------- Report ----------
order=['A1','A2','A3','A4','A5','F','EI','T','R']
print('=== Witness matrix (A3 strict, F eq, EI strong) ===')
print(f"{'':6s}"+" ".join(f"{k:>5s}" for k in order))
for n,M in W.items():
    r=check(M)
    print(f"{n:6s}"+" ".join(f"{str(r[k])[0]:>5s}" for k in order))

print('\n=== Decision checks ===')
# D1 total composition vs typing: any type-mismatched pair violates A1 under totality
M=W['W1']
bad=[(a,b) for a in M[1] for b in M[1] if M[3][a]!=M[2][b]]
print(f"D1 partial compose: {len(bad)} type-mismatched pairs (e.g. {bad[0]}) -> total comp + A1 UNSAT. PARTIAL wins.")
# D2 total inverse: W2p admits no total inverse assignment satisfying coherence
M=W['W2p']; ids=identities(M)
noinv=[c for c in M[1] if not any(M[4].get((c,d))==ids[M[2][c]] and M[4].get((d,c))==ids[M[3][c]] for d in M[1])]
print(f"D2 relational inverse: W2p contacts with no coherent inverse candidate: {noinv} -> total inverse op excludes W2p. RELATIONAL wins.")
# D3 step relation vs function
r=check(W['W4'])
print(f"D3 step as relation: W4 (two outcomes from one state) core-consistent: A1..A5={[r[k] for k in ['A1','A2','A3','A5']]}. FUNCTION would exclude it. RELATION wins.")
# D4 undo quantifier separation
r6s=check(W['W6'],EImode='strong')['EI']; r6b=check(W['W6'],EImode='bisim')['EI']; r6w=check(W['W6'],EImode='w1')['EI']
print(f"D4 undo quantifiers: W6 -> strong={r6s}, w1={r6w}, bisim={r6b} (return-to-copy separates bisim from strong/w1).")
# D5 F equality vs inclusions
r7a_sub=check(W['W7a'],Fmode='sub')['F']; r7a_eq=check(W['W7a'],Fmode='eq')['F']
r7b_sup=check(W['W7b'],Fmode='sup')['F']; r7b_eq=check(W['W7b'],Fmode='eq')['F']
print(f"D5 F: W7a decorative-composite passes sub({r7a_sub}) fails eq({r7a_eq}); W7b magic-composite passes sup({r7b_sup}) fails eq({r7b_eq}). EQUALITY wins (no junk, no magic).")
# D6 enabled/step split
r8=check(W['W8'])
idle=[(c,s) for (c,s) in W['W8'][8] if not any(cc==c and ss==s for (cc,ss,t) in W['W8'][9])]
print(f"D6 availability/execution split: W8 idle-availability pairs {idle} core-consistent (A5={r8['A5']}); merged signature cannot express. SPLIT wins.")

print('\n=== Theorem check: core+A3(strict)+A4+F(eq) entails EI(strong) ===')
for n in ['W1','W12']:
    r=check(W[n]); hyp=all(r[k] for k in ['A1','A2','A3','A4','A5','F'])
    print(f"{n}: hypotheses={hyp}, EI-strong={r['EI']}")
r11=check(W['W11'],A3mode='loose')
print(f"W11 (A3 LOOSE): A3loose={r11['A3']}, F-eq={r11['F']}, EI-strong={r11['EI']} -> loose identities break the derivation; STRICT A3 required.")

print('\n=== Bonus: R (return) vs A4 (invertibility) ===')
r=check(W['W2p'])
print(f"W2p: A4={r['A4']} but R={r['R']}, T={r['T']} -> return is reachability, strictly weaker than invertibility.")
