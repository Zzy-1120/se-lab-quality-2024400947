def calculate_area_and_perimeter_square(side):
    # 重复的计算逻辑
    area = side * side
    perimeter = 4 * side
    print(f"正方形面积是: {area}")
    print(f"正方形周长是: {perimeter}")
    return area, perimeter

def calculate_area_and_perimeter_rectangle(length, width):
    # 这里的逻辑和上面的函数非常相似，产生了重复代码
    area = length * width
    perimeter = 2 * (length + width)
    print(f"长方形面积是: {area}")
    print(f"长方形周长是: {perimeter}")
    return area, perimeter

# 一个过长的函数 (Long Method)
def generate_report():
    print("开始生成报告...")
    # 模拟很多重复的步骤
    step1 = 1 + 1
    print(f"步骤1结果: {step1}")
    step2 = 2 + 2
    print(f"步骤2结果: {step2}")
    step3 = 3 + 3
    # ... 假设这里还有20行类似的重复代码
    for i in range(10):
        print(f"处理第{i}步")
    print("报告生成结束。")

if __name__ == "__main__":
    calculate_area_and_perimeter_square(5)
    calculate_area_and_perimeter_rectangle(4, 6)
    generate_report()
