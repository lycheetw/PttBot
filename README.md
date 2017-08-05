# PttBot
```python
import PttBot

success = PttBot.login(acc, pw)
if not success:
    print("登入失敗")
    return

PttBot.write("s")
PttBot.write("Gossiping\r\n")
PttBot.functionKey("end")
PttBot.functionKey("right")
print(PttBot.read())
PttBot.logout()
```
## Run example
python3 example.py -acc your_account -pw your_password
