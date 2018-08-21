import os
def sendMail():
    sendmail_location = "/usr/sbin/sendmail" # sendmail location
    p = os.popen("%s -t" % sendmail_location, "w")
    p.write("From: %s\n" % "from@somewhere.com")
    p.write("To: %s\n" % "kumarhardik47@gmail.com")
    p.write("Subject: thesubject\n")
    p.write("\n") # blank line separating headers from body
    p.write("body of the mail")
    status = p.close()
    if status != 0:
           print "Sendmail exit status", status


sendMail()
