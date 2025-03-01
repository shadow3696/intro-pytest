import sys


def fibonacci_dynamic(n: int) -> int:
    fib_list = [0, 1]

    for i in range(1, n + 1):
        fib_list.append(fib_list[i] + fib_list[i - 1])

    print(f"mem size of fib_list is: {sys.getsizeof(fib_list)}")
    return fib_list[n]

def fibonacci_dynamic_v2(n: int) -> int:
    fib_1, fib_2 = 0, 1

    for i in range(1, n + 1):
        fi = fib_1 + fib_2
        fib_1, fib_2 = fib_2, fi

    return fib_1

"""
این دو تابع برای محاسبه‌ی اعداد فیبوناچی با استفاده از رویکردهای مختلف نوشته شده‌اند. در ادامه هرکدام رو توضیح می‌دم:

### 1. تابع `fibonacci_dynamic`

این تابع از روش "حفظ مقادیر قبلی" یا *Dynamic Programming* برای محاسبه‌ی عدد فیبوناچی استفاده می‌کند. در این روش تمام اعداد فیبوناچی از ابتدا تا عدد
فیبوناچی مورد نظر در یک لیست ذخیره می‌شوند. این روش زمان اجرا را کاهش می‌دهد، زیرا هر عدد فقط یک بار محاسبه می‌شود و به جای محاسبه مجدد از نتایج قبلی استفاده می‌شود.

**گام‌ها:**
- ابتدا یک لیست به نام `fib_list` ایجاد می‌کند که اولین دو عدد فیبوناچی (۰ و ۱) در آن قرار دارد.
- سپس از اندیس ۱ تا `n` برای هر عدد فیبوناچی، مقدار آن را با جمع دو عدد قبلی (که در `fib_list` ذخیره شده‌اند) محاسبه می‌کند و در انتهای لیست ذخیره می‌کند.
- در نهایت، با استفاده از `sys.getsizeof(fib_list)` اندازه حافظه مورد استفاده‌ی لیست `fib_list` را نمایش می‌دهد.
- عدد فیبوناچی nام را از لیست `fib_list` باز می‌گرداند.

**نکته مهم:**
- این روش حافظه‌ی زیادی مصرف می‌کند زیرا همه اعداد فیبوناچی از ابتدا تا nام را در لیست نگه می‌دارد.

### 2. تابع `fibonacci_dynamic_v2`

این تابع بهینه‌تر از نسخه‌ی اول عمل می‌کند و از حافظه کمتری استفاده می‌کند. به جای ذخیره‌ی همه‌ی اعداد فیبوناچی، فقط دو عدد آخر (یعنی fib_1 و fib_2) را ذخیره می‌کند و بقیه مقادیر را در همان زمان محاسبه می‌کند.

**گام‌ها:**
- ابتدا دو متغیر `fib_1` و `fib_2` را با مقدارهای ۰ و ۱ مقداردهی می‌کند که نشان‌دهنده‌ی دو عدد اول فیبوناچی هستند.
- سپس از اندیس ۱ تا `n` برای هر عدد فیبوناچی، آن را با جمع دو عدد قبلی محاسبه کرده و این دو عدد قبلی را به روز می‌کند.
- در پایان، `fib_1` که برابر با عدد فیبوناچی nام است را باز می‌گرداند.

**مزیت‌ها:**
- این روش حافظه‌ی کمتری مصرف می‌کند زیرا تنها دو متغیر برای ذخیره‌ی اعداد قبلی استفاده می‌شود.
- این نسخه سریع‌تر است و عملکرد بهتری دارد چرا که حافظه‌ی بیشتری مصرف نمی‌کند و فقط دو مقدار قبلی نگه‌داری می‌شود.

### مقایسه:
- تابع `fibonacci_dynamic` تمامی اعداد فیبوناچی از ابتدا تا nام را در یک لیست ذخیره می‌کند، اما تابع `fibonacci_dynamic_v2` فقط دو عدد آخر را ذخیره می‌کند و در نتیجه سریع‌تر و بهینه‌تر است.
"""