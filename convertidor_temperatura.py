class ConvertidorTemperatura :
    MaxCelsius = 100
    MaxFanhreint = 213
    MinFanhreint=31
    MinCelsius=-1

    @classmethod
    def c_f(cls,celsius):
        if celsius > cls.MaxCelsius:
            raise ValueError(f"Temperatura C demasiado alta:{celsius}")
        elif celsius < cls.MinCelsius:
            raise ValueError(f"Temperatura C demasiado baja:{celsius}")
        return celsius * 9/5 + 32

    @classmethod
    def f_c(cls,fahrenheint):
        if fahrenheint > cls.MaxFanhreint:
            raise ValueError(f"Temperatura F demasiada alta:{fahrenheint}")
        elif fahrenheint < cls.MinFanhreint:
            raise ValueError(f"Temperatura F demasiada baja:{fahrenheint}")
        return (fahrenheint-32)* 5/9

resultado = ConvertidorTemperatura.c_f(15)
print(f"15 C a F: {resultado:.2f}")
resultado = ConvertidorTemperatura.f_c(100)
print(f"100 F a C:{resultado:.2f}")