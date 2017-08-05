import PttBot
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-acc', action='store', dest='account',
        help='PTT account')
    parser.add_argument('-pw', action='store', dest='password',
        help='PTT password')

    results = parser.parse_args()
    acc = results.account
    pw = results.password
    if(acc is None or pw is None):
        return
    
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
    

if __name__ == "__main__":
    main()
