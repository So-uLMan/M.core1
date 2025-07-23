from mcore.core import MCore

if __name__ == "__main__":
    core = MCore(trust_list=["مصطفى"])
    print(core.respond("نفّذ الأمر الآن", sender="غريب"))  # يرفض
    print(core.respond("نفّذ الأمر الآن", sender="مصطفى"))  # ينفذ
