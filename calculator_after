# calculator_after.py
# 修复后：消除重复代码 + 拆分过长函数

# === 修复1：提取公共函数，消除重复代码 ===
def _print_area_and_perimeter(area, perimeter, shape_name):
    """通用的面积周长打印函数"""
    print(f"{shape_name}面积是: {area}")
    print(f"{shape_name}周长是: {perimeter}")
    return area, perimeter


def calculate_area_and_perimeter_square(side):
    """计算正方形的面积和周长"""
    area = side * side
    perimeter = 4 * side
    return _print_area_and_perimeter(area, perimeter, "正方形")


def calculate_area_and_perimeter_rectangle(length, width):
    """计算长方形的面积和周长"""
    area = length * width
    perimeter = 2 * (length + width)
    return _print_area_and_perimeter(area, perimeter, "长方形")


# === 修复2：将过长函数拆分成多个小函数 ===
def _print_report_header():
    """打印报告头部"""
    print("开始生成报告...")


def _process_step(step_num, value):
    """处理单个步骤"""
    print(f"步骤{step_num}结果: {value}")


def _process_loop():
    """处理循环部分"""
    for i in range(10):
        print(f"处理第{i}步")


def _print_report_footer():
    """打印报告尾部"""
    print("报告生成结束。")


def generate_report():
    """生成完整报告（现在是清晰的调度函数）"""
    _print_report_header()
    _process_step(1, 1 + 1)
    _process_step(2, 2 + 2)
    _process_step(3, 3 + 3)
    _process_loop()
    _print_report_footer()


if __name__ == "__main__":
    calculate_area_and_perimeter_square(5)
    calculate_area_and_perimeter_rectangle(4, 6)
    generate_report()
