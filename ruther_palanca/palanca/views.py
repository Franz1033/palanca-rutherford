import re
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from .models import Entry


items = [{"name" :"Amores, Carl", "email" : "nikkoboyamoress@gmail.com"}, {"name" :"Bajo, Jake", "email" : "jakebajo21@gmail.com"},{"name" :"Bustaliño, Aidan", "email" : "SoheeGT0912@gmail.com"},
        {"name" :"Elumba, Lemuel", "email" : "lemuelelumba0729@gmail.com"}, {"name" :"Garcia, Rudz", "email" : "rudzcullin12@gmail.com"},{"name" :"Herrera, Germaine", "email" : "germaineconan24@gmail.com"},
        {"name" :"Locsin, Jojene", "email" : "ianlocsin70@gmail.com"}, {"name" :"Macatual, Cyril", "email" : "cyilmacatual14@gmail.com "}, {"name" :"Omaguing, Micole", "email" : "omaguing.nino007@gmail.com"},
        {"name" :"Orong, Marc", "email" : "marcorong.03@gmail.com "}, {"name" :"Vergara, Jon", "email" : "Vergarajon30@gmail.com"}, {"name" :"Villejo, Luigi", "email" : "villejolm@gmail.com"},
        {"name" :"Zapanta, Franz", "email" : "franzzapanta1033@gmail.com"}, {"name" :"Alicante, Justine", "email" : "mizukijustine@gmail.com"}, {"name" :"Banawan, Treshia", "email" : "treshiamae07@gmail.com"}, 
        {"name" :"Dengal, Arnee", "email" : "arneedengal4@gmail.com "}, {"name" :"Duhaylungsod, Mabel", "email" : "mabelduhaylungsod@gmail.com"}, {"name" :"Euhengco, Heart", "email" : ""},
        {"name" :"Luce, Kate", "email" : ""}, {"name" :"Mira, Keren", "email" : ""}, {"name" :"Morandarte, Sol", "email" : "morandartesol@gmail.com"}, {"name" :"Pacuyao, Ruth", "email" : "hisokagobrrt@gmail.com"},
        {"name" :"Panong, Kylla ", "email" : ""}, {"name" :"Salas, Marnie", "email" : ""}, {"name" :"Sinconiegue, Gale", "email" : ""}, {"name" :"Sorronda, Melanie", "email" : "sorrondamelanie@gmail.com"}, 
        {"name" :"Tabañag, Althea", "email" : "tabanagag@gmail.com"}, {"name" :"Villadarez, Niña", "email" : "villadareznn@gmail.com"}]

def index(request):
    entries = len(Entry.objects.all())
    return render(request, "palanca/index.html", {"entries":entries})

def submit(request):
    if request.method == "POST":
        recipient = request.POST.get("recipient")
        code_name = request.POST.get("code_name")
        message = request.POST.get("message")

        names = []
        for item in items:
            names.append(item["name"])

        if recipient not in names:
            return JsonResponse({"error": f"Recipient with name '{recipient}' does not exist."}, status=400)

        else:
            entry = Entry(recipient=recipient, code_name=code_name, message=message)
            entry.save()
            for item in items:
                if item["name"] == recipient:
                    recipient = item["email"]
              
        send_mail(
            f"Rutherford Palanca Letter",
            f"From ({code_name}):\n\n{message}", 
            "Franz Mauri <FranzZ1033@gmail.com>",
            [recipient],
        )

        return HttpResponseRedirect(reverse("index"))


#host webapp
#create a new email add
