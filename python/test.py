# from email.message import EmailMessage
# import ssl 
# import smtplib

# email_sender='maheshdevani034@gmail.com'
# email_pass='icbfgnyomkurvtcw'

# email_rec='d.e.v.i.l.010.111.001@gmail.com'

# subject='the mail sent'

# body='''this 
# is 
# my
# mail
# ?
# '''

# em=EmailMessage()
# em['Form']=email_sender
# em['To']=email_rec
# em['subject']=subject
# em.set_content(body)

# context=ssl.create_default_context()
# with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
#     smtp.login(email_sender, email_pass)
#     smtp.sendmail(email_sender, email_rec, em.as_string())

# a=[1,
#     ['a','b','c']
# ]

# print(a[1[]])

# print(type(list))

# a={'a','b','c'}
# a=a.pop()
# print(a)

li=[1,2,3]

del li[-1]
print(li)