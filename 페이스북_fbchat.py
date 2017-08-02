from fbchat import Client

fc = Client('@gmail.com', '')
friends = fc.searchForUsers('')
friend = friends[0]
sent = fc.sendMessage("왕님이 이제 밥묵는다 함 - By Python", thread_id=friend.uid)
if sent:
    print("Message sent successfully!")
