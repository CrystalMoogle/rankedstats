from __future__ import division
import urllib
import json
import time

def usage_stats(url1, url2, weighting, response=None):
    try:
        weighting = int(weighting)
    except:
        return showerror("Weighting must be a valid integar", response)
    weighting1 = 1 / (weighting + 1)
    weighting2 = 1 - weighting1
    output = []
    objecta = {}
    try:
        stats1 = urllib.urlopen(url1).read()
        stats2 = urllib.urlopen(url2).read()
    except:
        return showerror("Please enter valid URLs", response)
    stats1 = stats1.replace("Mr. Mime", "MrMime").replace("Mime Jr.", "MimeJr")
    stats2 = stats2.replace("Mr. Mime", "MrMime").replace("Mime Jr.", "MimeJr")
    stats1 = stats1.split("\n")
    stats2 = stats2.split("\n")
    for x in range(0, len(stats1) - 1):
        string = stats1[x].split(" ")
        try:
            objecta[string[0]] = string[1]
        except:
            return showerror("Please enter URLs to the ranked stats file", response)

    for x in range(0, len(stats2) - 1):
        string = stats2[x].split(" ")
        if objecta.get(string[0]):
            result1 = float(objecta[string[0]]) * weighting2
        else:
            result1 = 0
        result2 = float(string[1]) * weighting1
        try:
            float(result1)
        except:
            result1 = 0
        try:
            float(result2)
        except:
            result2 = 0
        obj = {}
        obj["pokemon"] = string[0]
        obj["usage"] = result1 + result2
        output.append(obj)

    output = sorted(output, key=lambda k: k["usage"], reverse=True)
    toSend = ""
    for x in range(0, len(output) - 1):
        toSend += output[x]["pokemon"].replace("MrMime", "Mr. Mime").replace("MimeJr", "Mime Jr.") + " " + str(output[x]["usage"]) + "\n"
    if response == "json":
        return json.dumps({"response":output, "timestamp": time.time()})
    if response == "txt" or response == "text":
        return toSend
    return "<pre>" + toSend + "</pre>"
    
def showerror(errortype, response):
    if response == "json":
        return json.dumps({"Invalid Request":errortype})
    if response == "txt" or response == "text":
        return "Invalid Request: " + errortype
    return ["Invalid Request", errortype]
