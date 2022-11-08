from notificat.slack import Slack


if __name__ == "__main__":
    token = "xoxb-4298335007764-4308523227089-MEpC3RAsoiK7xt4OI4eQNo0o"
    ch_id = "C0492F5GH9P"
    
    slakcapi = Slack(token)
    
    slakcapi.send(ch_id, "test")