from PL26 import Question
q=["was it monica?\n(a)yes\n(b)no\n","was it phoebe?\n(a)yes\n(b)no\n","was it rachel?\n(a)yes\n(b)no\n"]
questions=[
    Question(q[0],"a"),
    Question(q[1],"b"),
    Question(q[2],"a"),
]
def test(questions):
    s=0
    for qs in questions:
        ans=input(qs.question)
        if ans==qs.answer:
            s+=1
    print("you got: "+str(s)+ "/"+str(len(questions)))
test(questions)
