# def paling_dekat(nilai, target):
#   selisih_terkecil = float('inf')
#   nilai_terdekat = None

#   for target_item in target:
#     selisih_absolut = abs(nilai - target_item)
#     if selisih_absolut < selisih_terkecil:
#       selisih_terkecil = selisih_absolut
#       nilai_terdekat = target_item

#   return nilai_terdekat

# var_1 = 1.9889888
# var_2 = 1.688

# target = [1.9898989, 1.7777777, 1.7666666, 1.5, 1.4]

# nilai_terdekat = paling_dekat(var_1, target)
# print(f"Nilai yang paling mendekati var_1 dari {target} adalah {nilai_terdekat}.")

# nilai_terdekat = paling_dekat(var_2, target)
# print(f"Nilai yang paling mendekati var_2 dari {target} adalah {nilai_terdekat}.")


def paling_dekat(nilai):
    selisih_terkecil = float('inf')
    nilai_terdekat = None
    # 21:9, 16:9, 16:10, 1:1, 4:3
    target = [2.3636364, 1.7777778, 1.6, 1, 1.3333333]

    for target_item in target:
        selisih_absolut = abs(nilai - target_item)
        if selisih_absolut < selisih_terkecil:
            selisih_terkecil = selisih_absolut
            nilai_terdekat = target_item

    return nilai_terdekat

var_1 = 1.9889888
var_2 = 1.688

nilai_terdekat = paling_dekat(var_1)
print(f"Nilai yang paling mendekati var_1 dari adalah {nilai_terdekat}.")

nilai_terdekat = paling_dekat(var_2)
print(f"Nilai yang paling mendekati var_2 dari  adalah {nilai_terdekat}.")
