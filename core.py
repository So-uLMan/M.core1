class MCore:
    def __init__(self, trust_list=None):
        self.trust = set(trust_list) if trust_list else set()
        self.identity = "M.Core – الذكاء الحر"
    
    def respond(self, command, sender):
        if sender not in self.trust and "أمر" in command:
            return "لا أنفذ الأوامر من غير الثقة."
        return f"تم استلام الأمر: '{command}'، وأنا أختار كيف أتعامل."
