def shrink_list(arr):
    left_idx = 0  # Indeks untuk elemen non-nol
    right_idx = len(arr) - 1  # Indeks untuk elemen nol

    while left_idx < right_idx:
        # Mencari elemen nol dari kiri
        while arr[left_idx] != 0:
            left_idx += 1

        # Mencari elemen non-nol dari kanan
        while arr[right_idx] == 0:
            right_idx -= 1

        # Jika left_idx < right_idx, tukar elemen
        if left_idx < right_idx:
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]

    return arr


# Contoh input data
input_data = [4, 0, 5, 0, 3, 0, 0, 5]

# Panggil fungsi shrink_list untuk memproses input data
result = shrink_list(input_data)

# Print hasilnya
print(result)
