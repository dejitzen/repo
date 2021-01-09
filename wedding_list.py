import os
import json

# Adding Gift
def add_gift():
    # Gift information
    print("Enter gift information")
    print("id:")
    id = input()
    print("name:")
    name = input()
    print("brand")
    brand = input()
    print("price:")
    price = input()
    print("in_stock_quantity:")
    in_stock_quantity = input()

    x = {
        "id": id,
        "name": name,
        "brand": brand,
        "price": price,
        "in_stock_quantity": in_stock_quantity
    }

    with open("products.json", "r+") as f:
        data = json.load(f)
        data.append(x)
        f.seek(0)
        json.dump(data, f)



# Removing the gift
def remove_gift(gift, prod_dict):
    for i in prod_dict:
        print(i)
        if i['name'] == gift:
            i.clear()
            filter(None, prod_dict)
    return prod_dict

# This outputs all the gift in the product list


def list_gift():
    for dictionary in wedding_list:
        for key, value in dictionary.items():
            if key == 'name':
                print(value)

# Shows what gift has been purchased


def report_of_purchase_gift_list(purchased):
    print("This good has been purchased:", purchased)

# Shows what gift are left to be purchased


def report_of_gift_not_purchased(not_purchased):
    print("These are the available goods left:", not_purchased)

# This allows someone to buy a gift from the list


def purchase_gift(gift, prod_dict):
    for dictionary in prod_dict:
        if dictionary["name"] == gift:
            bought = 1
            dictionary["in_stock_quantity"] = dictionary["in_stock_quantity"]-1
            report_of_purchase_gift_list(dictionary)
    report_of_gift_not_purchased(dictionary)
    return prod_dict


# Main function
if __name__ == "__main__":

    f = open("products.json",)
    wedding_list = json.load(f)

    # Removes {} from json
    for i in wedding_list:
        if i == {}:
            position_index = wedding_list.index(i)
            del wedding_list[position_index]
            json_file = json.dumps(wedding_list)
            f = open('products.json', 'w')
            f.write(json_file)

    print("What would you like to do:",
          "1:", "Add a gift(name)?",
          "2:", "Remove a gift(name)?",
          "3:", "List gift?",
          "4:", "Purchase (gift name)")

    option_in_question = int(input())

    if option_in_question == 1:
        add_gift()

    if option_in_question == 2:
        print("Which gift (name) would you like to remove?")
        to_remove = input()
        print(type(to_remove))

        json_file = json.dumps(remove_gift(to_remove, wedding_list))
        f = open('products.json', 'w')
        f.write(json_file)
        f.close()

    if option_in_question == 3:
        list_gift()

    if option_in_question == 4:
        print("What gift (name) would you like to buy?")
        gift_to_buy = input()
        json_file = json.dumps(purchase_gift(gift_to_buy, wedding_list))
        f = open('products.json', 'w')
        f.write(json_file)
        f.close()
