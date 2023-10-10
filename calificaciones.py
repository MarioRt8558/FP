def nota_teoria(t1,t2):
    t1=a_cero(t1)
    t2=a_cero(t2)
    res = (t1+t2)/ 2 
    if res< 4:
        res = 0
    return res

def a_cero(valor):
    res=valor
    if valor == None:
        res = 0
    return res


def nota_cuatrimestre(t,p):
    t1 = a_cero(t[0])
    t2 = a_cero(t[1])
    p = a_cero(p)
    if nota_teoria(t1,t2)>=4:
        res= 0.1*t1 + 0.1*t2 + 0.8*p
    else:
        res = 0
    return res

def nota_continua(notas_teoria, notas_practica):
    #Opcion 1
    t1 = notas_teoria[0]
    t2 = notas_teoria[1]
    p= notas_practica[0]
    c1 = nota_cuatrimestre([t1,t2],p)
    #Opcion 2
    c1 = nota_cuatrimestre(notas_teoria[:2], notas_practica[0])
    c2 = nota_cuatrimestre(notas_teoria[2:], notas_practica[1])
    res = (c1+c2)/2
    if c1 < 4 or c2 < 4:
        res = min(4,res)
    return res 