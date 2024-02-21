fin = open("APIs.txt","r+") 
api = fin.readlines()

api.pop(-1)

for i in range(0,len(api)):
  api[i] = api[i][:-1]
  api[i]=api[i]+'&'
  api[i]=api[i].split(':')
  api[i][1]=api[i][1].split('=')
  api[i][1].pop(0)
  for j in range(0,len(api[i][1])):
    api[i][1][j]=api[i][1][j].split('&')
    api[i][1][j].pop(1)
  api[i][1] = [ item for elem in api[i][1] for item in elem]

fin.close()

#s2 <- get.Comtrade(maxrec="502", type="C", freq="A", px="HS", ps="all", r="586", p="699%2C4%2C156%2C364", rg="2%2C1", cc="TOTAL", fmt="csv")
#lapply(s2[2], function(x) write.table(data.frame(x), file="data.csv", append = TRUE, sep = ",", na="", col.names=!file.exists("data.csv")))
out = open("scripts.txt","w")
out.close()

out = open("scripts.txt","w")
for i in range(0,len(api)):
  script="s2 <- get.Comtrade(maxrec=\""+api[i][1][0]+"\", type=\""+api[i][1][1]+"\", freq=\""+api[i][1][2]+"\", px=\""+api[i][1][3]+"\", ps=\""+api[i][1][4]+"\", r=\""+api[i][1][5]+"\", p=\""+api[i][1][6]+"\", rg=\""+api[i][1][7]+"\", cc=\""+api[i][1][8]+"\", fmt=\"csv\")\n"
  out.write(script)
  apply="lapply(s2[2], function(x) write.table(data.frame(x), file=\""+api[i][0]+".csv\", append = TRUE, sep = \",\", na=\"\", col.names=!file.exists(\""+api[i][0]+".csv\")))\n"
  out.write(apply)
out.close()