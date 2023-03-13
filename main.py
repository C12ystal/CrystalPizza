from tkinter import *

from PIL import Image, ImageTk

import datetime

my_label, images, status, color = {}, {}, {}, {}

cart = open("cart.txt", 'w')

total_price, price, base, nop, nod, background_label, new, image_margherita, image_turk, image_classic, nodt, cart_exp, \
    clear_message = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "", "Clear Cart"

extras = (
    'Tiramisu', 'Pudding', 'Profiterol', 'Suffle', 'Macaron', 'Kadayıf', 'Baklava', 'Magnolia', 'Ice Cream',
    'Cheesecake', 'Fries', 'Chicken Nuggets')

drinks = ('Coke', 'Pepsi', 'Orange Juice', 'Ayran', 'Sprite', 'Fanta', 'Ice Tea')

sauces = ('Ketchup', 'Mayonnaise', 'Mustard', 'Barbeque Sauce', 'Ranch Sauce')

pizza_ingredients = ('Goat Cheese', 'Meat',
                     'Cheese', 'Tomato', 'Mushroom', 'Sausage', 'Sweetcorn', 'Basil', 'Green pepper', 'Garlic',
                     'Onion',
                     'Pepperoni', 'Black olives')

prices = {'Goat Cheese': 20, 'Meat': 20, 'Ketchup': 1, 'Mayonnaise': 1, 'Mustard': 1, 'Barbeque Sauce': 1,
          'Ranch Sauce': 1,
          'Cheese': 15, 'Pepperoni': 10, 'Mushroom': 13, 'Sausage': 11, 'Onion': 8, 'Sweetcorn': 3,
          'Black olives': 7, 'Green pepper': 9, 'Garlic': 6, 'Tomato': 8, 'Basil': 12, 'Coke': 4, 'Pepsi': 4,
          'Orange Juice': 6, 'Ayran': 4, 'Sprite': 4, 'Fanta': 4, 'Ice Tea': 5,
          'Tiramisu': 16, 'Pudding': 8, 'Profiterol': 12,
          'Suffle': 16, 'Macaron': 5, 'Cheesecake': 16, 'Kadayıf': 12, 'Baklava': 16, 'Magnolia': 10, 'Ice Cream': 5,
          'Fries': 5, 'Chicken Nuggets': 10}


def main():
    root = Tk()
    root.configure(bg="#fcfcfc")
    height = int(root.winfo_screenheight())
    width = int(root.winfo_screenwidth())
    root.attributes('-fullscreen', True)
    bg = PhotoImage(file="background.png")

    for a in ('margherita', 'turk', 'classic', 'drinks', 'extras', 'checkout', 'custom'):
        images[a] = ImageTk.PhotoImage(
            Image.open(f"{a}.png").resize((int(width * 0.2562225475841874), int(height * 0.3515625)), Image.LANCZOS))

    def main_menu():
        forget_buttons()
        background()
        button_pizza = Button(root, fg="#341691", font="arial, 9 bold", text="Pizzas", bg='white',
                              width=int(width * 0.036), height=int(height * 0.00390625),
                              command=lambda: [forget_buttons(), background(), pizza_type_buttons()])
        nop_label = Label(root, text=nop, font=f"arial, {int(width / 50)} bold", bg='white', )
        button_extras = Button(root, fg="#341691", font="arial, 9 bold", text="Extras", bg='white',
                               width=int(width * 0.036), height=int(height * 0.00390625),
                               command=lambda: [reset_status(), forget_buttons(),
                                                add_base('Extra'),
                                                options(extras)])
        button_checkout = Button(root, fg="#341691", bg="light blue", font="arial, 9 bold", text="Checkout",
                                 width=int(width * 0.036), height=int(height * 0.00390625),
                                 command=lambda: [forget_buttons(), checkout_screen()])
        button_drinks = Button(root, fg="#341691", font="arial, 9 bold", text="Drinks", bg='white',
                               width=int(width * 0.036), height=int(height * 0.00390625),
                               command=lambda: [forget_buttons(), add_base('Drink'),
                                                options(drinks)])
        exit_button = Button(root, bg='red', font="arial, 15 bold", text='x', width=2,
                             height=1, fg='white',
                             command=lambda: [cart.write("\n-abandoned-"), cart.close(), root.destroy()])
        exit_button.place(x=width - width / 35, y=width / 300)
        button_pizza.place(x=width * 0.23, y=width * 0.22)
        nop_label.place(x=width * 0.20, y=width * 0.22)
        button_extras.place(x=width * 0.23, y=width * 0.48)
        button_drinks.place(x=width * 0.53, y=width * 0.22)
        button_checkout.place(x=width * 0.53, y=width * 0.48)

        image_pizzas = Label(root, image=images['classic'])
        image_pizzas.place(x=width * 0.23, y=width * 0.02)
        image_drinks = Label(root, image=images['drinks'])
        image_drinks.place(x=width * 0.53, y=width * 0.02)
        image_extras = Label(root, image=images['extras'])
        image_extras.place(x=width * 0.23, y=width * 0.28)
        image_checkout = Label(root, image=images['checkout'])
        image_checkout.place(x=width * 0.53, y=width * 0.28)

    def reset_status():
        global status, color, clear_message
        for i in pizza_ingredients + sauces:
            status[i] = 'No'
            color[i] = 'Gray'
        for i in drinks + extras:
            status[i] = '+'
            color[i] = 'Gray'
        color['clear'] = 'Orange'
        clear_message = 'Clear Cart'

    reset_status()

    def comp_price():
        global price
        if base == 'Drink' or base == 'Extra':
            price = 0
            for i in status:
                if status[i] == "1L" or status[i] == "1 Serving of":
                    price += prices[i] * 1.00
                elif status[i] == "2.5L" or status[i] == "2 Servings of":
                    price += prices[i] * 2.00
        else:
            if base == 'custom':
                price = 40
            else:
                price = 20
            for i in pizza_ingredients:
                if status[i] == "With":
                    price += prices[i] * 1.00
                elif status[i] == "Extra":
                    price += prices[i] * 1.50
            for i in sauces:
                if status[i] == "1 Packet of":
                    price += prices[i] * 1.00
                elif status[i] == "2 Packets of":
                    price += prices[i] * 2
        price_label = Label(root, text=f"   Total amount : {price}   ", bg='#fcfcfc', fg='#341691', font=('ariel', 20))
        price_label.grid(row=3, column=5, padx=(width * 0.1565841874084919, 0), pady=(width * 0.06, 0))

    def enable_buttons(ingredients):
        for i in pizza_ingredients + sauces + drinks + extras:
            if i not in ingredients:
                color[i] = 'gray'
                status[i] = 'Disabled'

    def lock_buttons(ingredients):
        global status
        if base == 'Drink':
            for i in drinks:
                if nod == nop:
                    if i not in ingredients:
                        my_label[i].configure(state=DISABLED)
                        status[i] = 'Disabled'
                else:
                    if i not in ingredients:
                        status[i] = '+'
                        my_label[i].configure(state=NORMAL, text=f"{status[i]} {i}")
        else:
            for i in extras:
                if nodt == nop:
                    if i not in ingredients:
                        my_label[i].configure(state=DISABLED)
                        status[i] = 'Disabled'
                else:
                    if i not in ingredients:
                        status[i] = '+'
                        my_label[i].configure(state=NORMAL, text=f"{status[i]} {i}")

    def add_base(pizza_type):
        global base
        base = 0
        base = pizza_type
        color[base] = "lime"
        background()

    def add_ingredient(ingredient):
        global nod, nodt
        if type(ingredient) == tuple:
            for i in ingredient:
                add_ingredient(i)
        else:
            if base != 'Drink':
                if ingredient not in sauces and ingredient not in extras:
                    if status[ingredient] != "With" and status[ingredient] != "Extra":
                        status[ingredient] = "With"
                        color[ingredient] = "#1d1691"
                    elif status[ingredient] != "Extra":
                        status[ingredient] = "Extra"
                        color[ingredient] = "#341691"
                    else:
                        status[ingredient] = "No"
                        color[ingredient] = "gray"
                elif ingredient in sauces:
                    if status[ingredient] != "1 Packet of" and status[ingredient] != "2 Packets of":
                        status[ingredient] = "1 Packet of"
                        color[ingredient] = "#1d1691"
                    elif status[ingredient] != "2 Packets of":
                        status[ingredient] = "2 Packets of"
                        color[ingredient] = "#341691"
                    else:
                        status[ingredient] = "No"
                        color[ingredient] = "gray"
                else:
                    if status[ingredient] != "1 Serving of":
                        status[ingredient] = "1 Serving of"
                        color[ingredient] = "#1d1691"
                        nodt += 1
                    else:
                        status[ingredient] = "+"
                        color[ingredient] = "gray"
                        nodt -= 1

                    selected_extras = []
                    for i in status:
                        if status[i] == "1 Serving of":
                            selected_extras.append(i)

                    if nodt == nop:
                        lock_buttons(selected_extras)
                    else:
                        lock_buttons(selected_extras)
            else:
                if status[ingredient] != "1L" and status[ingredient] != "2.5L":
                    status[ingredient] = "1L"
                    color[ingredient] = "#1d1691"
                    nod += 1
                elif status[ingredient] != "2.5L":
                    status[ingredient] = "2.5L"
                    color[ingredient] = "#341691"
                else:
                    status[ingredient] = "+"
                    color[ingredient] = "gray"
                    nod -= 1

                selected_drinks = []
                for i in status:
                    if status[i] in ("1L", "2.5L"):
                        selected_drinks.append(i)

                if nod == nop:
                    lock_buttons(selected_drinks)
                else:
                    lock_buttons(selected_drinks)

    background_label = Label(root, image=bg)

    background_label.place(x=0, y=0)

    def options(opts):
        y = 0
        x = 0
        if base not in ('Drink', 'Extra'):
            enable_buttons(opts)
            for i in opts:
                my_label[i] = Button(root, fg="white", font="TimesNewRoman 8 bold", text=f"{status[i]} {i}",
                                     width=int(width * 0.017625),
                                     height=int(height * 0.0027777777777778), bg=color[i],
                                     command=lambda i=i: [add_ingredient(i),
                                                          my_label[i].configure(bg=color[i], text=f"{status[i]} {i}"),
                                                          comp_price()])
                if y == 0:
                    if x == 0:
                        my_label[i].grid(row=1, column=0 + x, padx=(width * 0.0565841874084919, 0),
                                         pady=(width * 0.109809663250366, 0))
                    else:
                        my_label[i].grid(row=1, column=0 + x, padx=(width * 0.0065841874084919, 0),
                                         pady=(width * 0.109809663250366, 0))
                    y += 1
                elif 0 < y <= 5:
                    if x == 0:
                        my_label[i].grid(row=1 + y, column=0 + x, padx=(width * 0.0565841874084919, 0),
                                         pady=(width * 0.059809663250366, 0))
                    else:
                        my_label[i].grid(row=1 + y, column=0 + x, padx=(width * 0.0065841874084919, 0),
                                         pady=(width * 0.059809663250366, 0))
                    y += 1
                if y == 5:
                    y = 0
                    x += 1

                back_label = Button(root, fg="white", font="TimesNewRoman 8 bold", text=f"Go Back",
                                    width=int(width * 0.015625),
                                    height=int(height * 0.0027777777777778), bg="red",
                                    command=lambda: [add_base(0), forget_buttons(),
                                                     reset_status(), background(),
                                                     pizza_type_buttons()])
                back_label.grid(row=5, column=5, padx=(width * 0.1565841874084919, 0),
                                pady=(width * 0.059809663250366, 0))

                add_cart_label = Button(root, fg="white", font="TimesNewRoman 8 bold", text=f"Add to Cart",
                                        width=int(width * 0.015625),
                                        height=int(height * 0.0027777777777778), bg="green",
                                        command=lambda: [add_to_cart(), add_base(0), forget_buttons(),
                                                         reset_status(), main_menu()])
                add_cart_label.grid(row=1, column=5, padx=(width * 0.1565841874084919, 0),
                                    pady=(width * 0.109809663250366, 0))

        else:
            for i in opts:
                if status[i] == 'Disabled':
                    my_label[i] = Button(root, fg="white", font="TimesNewRoman 8 bold", text=f"{status[i]} {i}",
                                         width=int(width * 0.017625),
                                         height=int(height * 0.0027777777777778), bg=color[i], state=DISABLED,
                                         command=lambda i=i: [add_ingredient(i),
                                                              my_label[i].configure(bg=color[i],
                                                                                    text=f"{status[i]} {i}"),
                                                              comp_price()])
                else:
                    my_label[i] = Button(root, fg="white", font="TimesNewRoman 8 bold", text=f"{status[i]} {i}",
                                         width=int(width * 0.015625),
                                         height=int(height * 0.0027777777777778), bg=color[i],
                                         command=lambda i=i: [add_ingredient(i),
                                                              my_label[i].configure(bg=color[i],
                                                                                    text=f"{status[i]} {i}"),
                                                              comp_price()])
                if y == 0:
                    if x == 0:
                        my_label[i].grid(row=1, column=0 + x, padx=(width * 0.0565841874084919, 0),
                                         pady=(width * 0.109809663250366, 0))
                    else:
                        my_label[i].grid(row=1, column=0 + x, padx=(width * 0.0065841874084919, 0),
                                         pady=(width * 0.109809663250366, 0))
                    y += 1
                elif 0 < y <= 5:
                    if x == 0:
                        my_label[i].grid(row=1 + y, column=0 + x, padx=(width * 0.0565841874084919, 0),
                                         pady=(width * 0.059809663250366, 0))
                    else:
                        my_label[i].grid(row=1 + y, column=0 + x, padx=(width * 0.0065841874084919, 0),
                                         pady=(width * 0.059809663250366, 0))
                    y += 1
                if y == 5:
                    y = 0
                    x += 1
            lock_buttons("")
            back_label = Button(root, fg="white", font="TimesNewRoman 8 bold", text=f"Go Back",
                                width=int(width * 0.015625),
                                height=int(height * 0.0027777777777778), bg="red",
                                command=lambda: [add_base(0), forget_buttons(),
                                                 background(),
                                                 main_menu()])
            back_label.grid(row=5, column=5, padx=(width * 0.1565841874084919, 0), pady=(width * 0.059809663250366, 0))
            if base == 'Drink':
                add_cart_label = Button(root, fg="white", font="TimesNewRoman 8 bold", text=f"Add to Cart",
                                        width=int(width * 0.015625),
                                        height=int(height * 0.0027777777777778), bg="green",
                                        command=lambda: [add_to_cart(), lock_buttons(""), forget_buttons(),
                                                         reset_status(), background(),
                                                         options(drinks), add_message()])
            else:
                add_cart_label = Button(root, fg="white", font="TimesNewRoman 8 bold", text=f"Add to Cart",
                                        width=int(width * 0.015625),
                                        height=int(height * 0.0027777777777778), bg="green",
                                        command=lambda: [add_to_cart(), lock_buttons(""), forget_buttons(),
                                                         reset_status(), background(), options(extras),
                                                         add_message()])
            add_cart_label.grid(row=1, column=5, padx=(width * 0.1565841874084919, 0),
                                pady=(width * 0.109809663250366, 0))

    def background():
        global background_label
        global new
        try:
            background_label.destroy()
        except AttributeError:
            pass
        if base in ('Classic', 'Turk', 'Custom', 'Margherita'):
            new = PhotoImage(file="choose.png")
            background_label = Label(root, image=new)
            background_label.place(x=0, y=0)
        else:
            new = PhotoImage(file="background.png")
            background_label = Label(root, image=new)
            background_label.place(x=0, y=0)

    def pizza_type_buttons():
        global image_margherita
        global image_turk
        global image_classic
        button_classic = Button(root, fg="#341691", font="arial, 9 bold", text="Classic Pizza",
                                width=int(width * 0.036), height=int(height * 0.00390625),
                                bg="white",
                                command=lambda: [add_base('Classic'), reset_status(),
                                                 add_ingredient(('Meat', 'Cheese',
                                                                 'Tomato', 'Mushroom',
                                                                 'Sausage', 'Sweetcorn',
                                                                 'Green pepper', 'Pepperoni',
                                                                 'Black olives')),
                                                 forget_buttons(), background(),
                                                 options(('Meat',
                                                          'Cheese', 'Tomato', 'Mushroom',
                                                          'Sausage', 'Sweetcorn',
                                                          'Green pepper',
                                                          'Pepperoni', 'Black olives') + sauces), comp_price()])
        button_turk_pizza = Button(root, fg="#341691", font="arial, 9 bold", text="Turkish Pizza",
                                   width=int(width * 0.036), height=int(height * 0.00390625),
                                   bg="white",
                                   command=lambda: [add_base('Turk'), reset_status(),
                                                    add_ingredient(
                                                        ('Tomato', 'Onion', 'Garlic', 'Green pepper', 'Basil', 'Meat')),
                                                    forget_buttons(), background(),
                                                    options(
                                                        ('Tomato', 'Onion', 'Garlic', 'Green pepper', 'Basil', 'Meat')),
                                                    comp_price()])
        button_custom = Button(root, fg="#341691", font="arial, 9 bold", text="Custom Pizza",
                               width=int(width * 0.036), height=int(height * 0.00390625),
                               bg="white",
                               command=lambda: [add_base('Custom'), reset_status(), add_ingredient(()),
                                                forget_buttons(), background(),
                                                options(pizza_ingredients + sauces), comp_price()])
        button_margherita = Button(root, fg="#341691", font="arial, 9 bold", text="Margherita Pizza",
                                   highlightcolor='black',
                                   width=int(width * 0.036), height=int(height * 0.00390625),
                                   bg="white",
                                   command=lambda: [add_base('Margherita'), reset_status(),
                                                    add_ingredient(('Tomato', 'Cheese', 'Basil', 'Garlic')),
                                                    forget_buttons(), background(),
                                                    options(('Tomato', 'Cheese', 'Basil', 'Garlic') + sauces),
                                                    comp_price()])
        main_menu_label = Button(root, fg="#341691", font="TimesNewRoman 8 bold", text=f"Main Menu",
                                 width=int(width * 0.036),
                                 height=int(height * 0.00390625), bg="light blue",
                                 command=lambda: [background(), reset_status(), main_menu()])
        main_menu_label.place(x=width * 0.68, y=width * 0.48)
        button_classic.place(x=width * 0.08, y=width * 0.22)
        button_turk_pizza.place(x=width * 0.08, y=width * 0.48)
        button_margherita.place(x=width * 0.38, y=width * 0.22)
        button_custom.place(x=width * 0.38, y=width * 0.48)

        image_margherita = Label(root, image=images['margherita'])
        image_margherita.place(x=width * 0.38, y=width * 0.02)
        image_classic = Label(root, image=images['classic'])
        image_classic.place(x=width * 0.08, y=width * 0.02)
        image_turk = Label(root, image=images['turk'])
        image_turk.place(x=width * 0.08, y=width * 0.28)
        image_custom = Label(root, image=images['custom'])
        image_custom.place(x=width * 0.38, y=width * 0.28)

    def forget_buttons():
        for widget in root.winfo_children():
            widget.destroy()

    def add_to_cart():
        global total_price, cart_exp, nop
        global cart
        total_price += price
        if "With" in status.values() or "Extra" in status.values() or "1L" in status.values() \
                or "2.5L" in status.values() or "1 Serving of" in status.values() or "2 Servings of" in status.values():
            if base not in ('Drink', 'Extra'):
                cart.write(f"\n{base} Pizza\n")
                cart_exp += f"\n{base} Pizza\n"
                for i in status:
                    if base != "Custom" and i not in sauces and status[i] != "Disabled":
                        cart.write(f"{status[i]} {i}\n")
                        cart_exp += f"{status[i]} {i}\n"
                    elif base != "Custom" and status[i] not in ("No", "Disabled"):
                        cart.write(f"{status[i]} {i}\n")
                        cart_exp += f"{status[i]} {i}\n"
                    elif status[i] not in ("No", "Disabled"):
                        cart.write(f"{status[i]} {i}\n")
                        cart_exp += f"{status[i]} {i}\n"
                nop += 1
            else:
                cart.write(f"\n{base}:\n")
                cart_exp += f"\n{base}:\n"
                for i in status:
                    if status[i] not in ("+", "No", "Disabled"):
                        cart.write(f"{status[i]} {i}\n")
                        cart_exp += f"{status[i]} {i}\n"
            cart.write(f"Price : {price}\n")
            cart_exp += f"Price : {price}\n"
        else:
            raise Exception("Gave Up")

    def checkout_screen():
        background()
        global tc_entry
        tc_label = Label(root, text="Social Security Number:", font='Arial, 24', bg='#fcfcfc')
        tc_entry = Entry(root, width=int(width / 100), font='Arial, 24')
        tc_label.grid(row=0, column=0, padx=width / 20, pady=(width / 7, width / 100))
        tc_entry.grid(row=1, column=0, padx=width / 20)
        global ccn_entry
        ccn_label = Label(root, text="Credit Card Number:", font='Arial, 24', bg='#fcfcfc')
        ccn_entry = Entry(root, width=int(width / 100), font='Arial, 24')
        ccn_label.grid(row=2, column=0, padx=width / 20, pady=width / 100)
        ccn_entry.grid(row=3, column=0, padx=width / 20)
        global ccv_entry
        ccv_label = Label(root, text="CCV:", font='Arial, 24', bg='#fcfcfc')
        ccv_entry = Entry(root, width=int(width / 100), font='Arial, 24')
        ccv_label.grid(row=4, column=0, padx=width / 100, pady=width / 100)
        ccv_entry.grid(row=5, column=0, padx=width / 100)
        global ccp_entry
        ccp_label = Label(root, text="Credit Card Password:", font='Arial, 24', bg='#fcfcfc')
        ccp_entry = Entry(root, width=int(width / 100), font='Arial, 24')
        ccp_label.grid(row=6, column=0, padx=width / 100, pady=width / 100)
        ccp_entry.grid(row=7, column=0, padx=width / 100)
        checkout_back_label = Button(root, fg="white", font="TimesNewRoman 8 bold", text=f"Go Back",
                                     width=int(width * 0.015625),
                                     height=int(height * 0.0027777777777778), bg="red",
                                     command=lambda: [forget_buttons(), main_menu()])
        checkout_back_label.grid(row=7, column=1)
        clear_label = Button(root, fg="white", font="TimesNewRoman 8 bold", text=clear_message,
                             width=int(width * 0.015625),
                             height=int(height * 0.0027777777777778), bg=color['clear'],
                             command=lambda: [clear_label.configure(bg='red', text='Are you sure?'), clean_cart()])
        clear_label.grid(row=4, column=1)

        cart_label_1 = Label(root, text=f"Total:{total_price}" + f"{cart_exp[:450]}", font='Arial 12', bg='#fcfcfc')
        cart_label_1.place(x=width * 0.48, y=width / 16)

        cart_label_2 = Label(root, text=f"{cart_exp[450:900]}", font='Arial 12', bg='#fcfcfc')
        cart_label_2.place(x=width * 0.65, y=width / 16)

        cart_label_3 = Label(root, text=f"{cart_exp[900:1350]}", font='Arial 12', bg='#fcfcfc')
        cart_label_3.place(x=width * 0.82, y=width / 16)

        purchase_label = Button(root, fg="white", font="TimesNewRoman 8 bold", text=f"Make Purchase",
                                width=int(width * 0.015625),
                                height=int(height * 0.0027777777777778), bg="green",
                                command=lambda: [checkout()])
        purchase_label.grid(row=1, column=1)

    def checkout():
        global cart_exp
        if nop >= 1:
            info = {'Social Security Number': tc_entry.get(), 'Credit Card Number': ccn_entry.get(),
                    'CCV': ccv_entry.get(),
                    'Credit Card Password': ccp_entry.get()}
            character_limit = {'Social Security Number': 11, 'Credit Card Number': 16, 'CCV': 3,
                               'Credit Card Password': 4}
            for i in ('Social Security Number', 'Credit Card Number', 'CCV', 'Credit Card Password'):
                if i != 'Credit Card Password':
                    if entry_int(character_limit[i], info[i], '='):
                        pass
                    else:
                        blank_label = Label(text="⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", bg='#fcfcfc')
                        blank_label.grid(row=20, column=0)
                        digit_error_label = Label(text=f"{i} must be {character_limit[i]} digits long!", bg='#fcfcfc',
                                                  fg='red')
                        digit_error_label.grid(row=20, column=0)
                        raise Exception("Gave Up")
                else:
                    if entry_int(character_limit[i], info[i], '>='):
                        pass
                    else:
                        blank_label = Label(text="⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", bg='#fcfcfc')
                        blank_label.grid(row=20, column=0)
                        digit_error_label = Label(text=f"Enter a valid {i}!", bg='#fcfcfc', fg='red')
                        digit_error_label.grid(row=20, column=0)
                        raise Exception("Gave Up")
            try:
                for i in info:
                    int(info[i])
                for i in info:
                    cart.write(f"\n{i}:\n{int(info[i])}")
            except ValueError:
                blank_label = Label(text="⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", bg='#fcfcfc')
                blank_label.grid(row=20, column=0)
                error_label = Label(root, text="All the characters must be numbers!", bg='#fcfcfc', fg='red')
                error_label.grid(row=20, column=0)
                raise Exception("Gave Up")
            cart.write(f"\nTotal Amount:{total_price}\n")
            cart_exp += f"\nTotal Amount:{total_price}\n"
            cart.write(f"\nTime:{str(datetime.datetime.now())}")
            cart.close()
            root.destroy()
        else:
            error_label = Label(root, text="You can't make an order without a pizza in it!", bg='#fcfcfc', fg='red')
            error_label.grid(row=20, column=0)

    def entry_int(character_limit, integer, mode):
        length = 0
        for i in integer:
            length += 1
        if mode == '=':
            if length != character_limit:
                return False
        else:
            if length < character_limit:
                return False
        return True

    def clean_cart():
        global clear_message, cart_exp, nop, nod, nodt, total_price
        if cart_exp != "":
            if clear_message != "Are you sure?":
                clear_message = "Are you sure?"
                color['clear'] = 'red'
            else:
                cart.truncate(0)
                cart_exp = ""
                clear_message = "Cart Cleared"
                color['clear'] = 'lime'
                total_price, nop, nod, nodt = 0, 0, 0, 0
                forget_buttons()
                checkout_screen()
                reset_status()

        else:
            raise Exception("Gave Up")

    def add_message():
        message_label = Label(root, text="Items have been added to your cart!", bg='#fcfcfc', fg='lime',
                              font=('ariel', 20))
        message_label.grid(row=3, column=5, padx=(width * 0.2065841874084919, 0), pady=(width * 0.06, 0))

    main_menu()
    root.mainloop()


main()
