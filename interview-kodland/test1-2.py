def shrink_list(arr):
    # Membuat list kosong untuk menyimpan elemen non-nol
    non_zero_elements = []

    # Mencari elemen non-nol dari list arr dan menyimpannya dalam non_zero_elements
    for x in arr:
        if x != 0:
            non_zero_elements.append(x)

    # Mencari jumlah elemen nol dalam list arr
    count_of_zeros = arr.count(0)

    # Membuat list berisi elemen nol sebanyak count_of_zeros
    zeros_list = [0] * count_of_zeros

    # Menggabungkan list elemen non-nol dan list elemen nol
    result_list = non_zero_elements + zeros_list

    # Mengembalikan hasil list yang sudah di-gabung
    return result_list

# Contoh input data
input_data = [4, 0, 5, 0, 3, 0, 0, 5]

# Panggil fungsi shrink_list untuk memproses input data
result = shrink_list(input_data)

# Print hasilnya
print(result)