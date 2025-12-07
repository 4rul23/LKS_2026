import asyncore
import smtpd


class CustomSMTPChannel(smtpd.SMTPChannel):
    """Custom channel to leak SMB creds via VRFY."""

    def smtp_VRFY(self, arg):
        arg_lower = (arg or "").lower().strip()
        if "smbuser@trailblazer.corp" in arg_lower:
            self.push(
                b"252 2.5.4 <smbuser@trailblazer.corp> [Desc: SMB Access / Pass: smbpass123]\r\n"
            )
        else:
            self.push(b"550 5.1.1 User unknown\r\n")


class CustomSMTPServer(smtpd.SMTPServer):
    channel_class = CustomSMTPChannel

    def process_message(self, peer, mailfrom, rcpttos, data):
        # Ignore mails, this service is only for VRFY/enum
        return


print("SMTP server starting on port 25...")
CustomSMTPServer(("0.0.0.0", 25), None)
asyncore.loop()
