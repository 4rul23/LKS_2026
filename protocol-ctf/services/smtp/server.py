import asyncore
import smtpd

class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        pass  # Ignore mails

    def smtp_VRFY(self, arg):
        arg_lower = arg.decode('ascii').lower().strip()
        if 'smbuser@trailblazer.corp' in arg_lower:
            # Simulate an information leak in the user description field
            self.push(b'252 2.5.4 <smbuser@trailblazer.corp> [Desc: SMB Access / Pass: smbpass123]\r\n')
        else:
            self.push(b'550 5.1.1 User unknown\r\n')

print("SMTP server starting on port 25...")
CustomSMTPServer(('0.0.0.0', 25), None)
asyncore.loop()
