def queen_movement(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return "YES"
    
    if abs(x1 - x2) == abs(y1 - y2):
        return "YES"
    
    return "NO"

while True:
    try:
        print("Input harus angka diantara 1 hingga 8")
        x1 = int(input())
        y1 = int(input())
        x2 = int(input())
        y2 = int(input())

        if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
            break
        else:
            print("Input harus berada di antara 1 dan 8. Coba lagi.")
    except ValueError:
        print("Input harus berupa angka. Coba lagi.")

result = queen_movement(x1, y1, x2, y2)
print(result)