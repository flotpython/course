### TO PUT IN THE NOTEBOOK (BEGIN)
df1 = pd.DataFrame(np.random.randint(1, 10, size=(2,2)), 
                  columns=list('ab'), 
                  index=list('xy'))

df2 = pd.DataFrame(np.random.randint(1, 10, size=(2,2)), 
                  columns=list('ab'), 
                  index=list('zt'))
### TO PUT IN THE NOTEBOOK (END)

# Commençons par regarder l'opération de concaténation.
# Lorsque j'ai DataFrame df1 et df2
print(df1)
print(df2)

# Je peux les concatener avec concat
# attention, on passe à concat une séquence d'objet à concaténer. 
# Concat() va par défaut concaténer sur les ligne en alignant les
# colonnes
pd.concat([p1, p2]) 

# On peut décider de concaténer les colonnes en alignant 
# les lignes avec l'argument axis
df1 = pd.DataFrame(np.random.randint(1, 10, size=(2,2)), 
                  columns=list('ab'), 
                  index=list('xy'))

df2 = pd.DataFrame(np.random.randint(1, 10, size=(2,2)), 
                  columns=list('cd'), 
                  index=list('xy'))
pd.concat([df1, df2], axis=1) 

# 2m20