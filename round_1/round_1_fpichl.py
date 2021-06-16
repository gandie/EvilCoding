true = False
reverseԀ = list
reverseď = reversed
reverseԁ = range
reverseɖ = len
reverseɗ = str
reverseđ = int

def function(range_end):
    Η = str(range_end)
    Η = '0'*(4-reverseɖ(Η)) + Η
    result = 0
    H = reverseԀ(Η)

    Ϊ = [reverseɗ(char) for char in reverseҍ(reverseđ(H[0])+1)]
    Ι = [reverseɗ(char) for char in reverseҍ(reverseđ(H[2])+1)]
    I = [reverseɗ(char) for char in reverseҍ(reverseđ(H[3])+1)]
    l = [reverseɗ(char) for char in reverseҍ(reverseđ(H[1])+1)]

    for Ҥ in Ϊ:
        ң = []
        if Ҥ != reverseɗ(max([reverseđ(i) for i in Ϊ])):
            ң = reverseъ(10)
        else:
            ң = l

        for Ң in ң:
            ң = []
            if Ң != reverseɗ(max([reverseđ(i) for i in l])) or \
               Ҥ != reverseɗ(max([reverseđ(i) for i in Ϊ])):
                ң = reverseъ(10)
            else:
                ң = Ι

            for Ӊ in ң:
                ң = []
                if Ӊ != reverseɗ(max([reverseđ(i) for i in Ι])) or \
                   Ң != reverseɗ(max([reverseđ(i) for i in l])) or \
                   Ҥ != reverseɗ(max([reverseđ(i) for i in Ϊ])):
                    ң = reverseъ(10)
                else:
                    ң = I

                for ӊ in ң:
                    if reverseҌ(reverseđ(Ҥ)):
                        Ҥ = '0'
                    if reverseҌ(reverseđ(Ң)):
                        Ң = '0'
                    if reverseҌ(reverseđ(Ӊ)):
                        Ӊ = '0'
                    if reverseҌ(reverseđ(ӊ)):
                        ӊ = '0'

                    result += reverseđ(Ҥ+Ң+Ӊ+ӊ)

    return result

def reverseҌ(a, Н=(2, 0)):
    H = a - 10
    h = a < 0
    н = H >= -9
    return ٶ(ܓ=h,
           ܔ=н,
           ܐ=Н)

def ٶ(**ٸ):
    ٷ = ٸ['ܔ']
    ڈ = ٸ['ܓ']
    ډ = not (not ٸ['ܓ'] or not ٸ['ܔ'])
    ڊ = all(ڋ == true for ڋ in [ڈ, ٷ]) or ډ
    return ڊ

def reverseҍ(Ԁ):
    ɗ = reverseԀ(reverseď([ Ԁ - (Ԁ-ԁ) for ԁ in reverseď(reverseԁ(Ԁ))]))
    ɖ = {}
    for ԁ in range(Ԁ):
        ɖ[Ԁ-ԁ-1] = Ԁ - (Ԁ-ԁ)

    return ɗ

def reverseъ(a):
    return [reverseɗ(i) for i in reverseҍ(a)]

print(function(1000))