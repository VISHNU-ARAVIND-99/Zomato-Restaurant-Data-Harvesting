# zomoto_web_scraping

main.py file contain code which uses selenium webdriver & BeautifulSoup to scrap restaurant data from Zomoto website in Json,

## Following Is The Example of data scraped of one restaurant :

https://raw.githubusercontent.com/VISHNU-ARAVIND-99/zomoto_web_scraping/main/output.json
I scraped 1166 restaurant data u can see in above link.

{
    "restaurant name": "SS Hyderabad Biryani",
    "restaurant_zomoto_link": "https://www.zomato.com/chennai/ss-hyderabad-biryani-parrys/",
    "description": "Biryani, Seafood, North Indian, Mughlai, Rolls, Chinese, Kebab",
    "location": "Parrys, Chennai",
    "opening_time": "11am – 10:30pm (Today)",
    "phone_num": "+919940119700",
    "location_google_map_link": "https://www.google.com/maps/dir/?api=1&destination=13.0896212574,80.2888832241",
    "location_address": "New 319, Old 154, Thambu Chetty Street, Parrys, Chennai",
    "dining_rating": "4.2",
    "delivery_rating": "4.4",
    "dining_rating_count": "183",
    "delivery_rating_count": "10.7K",
    "food_item_list": {
      "Hyderabadi Chicken Dum Biryani": {
        "food_price": "₹299",
        "food_rating_count": "1091 votes",
        "food_image_url": "http",
        "food_description": "Hyderabadi Chicken Dum Biryani"
      },
      "Chicken Biryani Executive Pack": {
        "food_price": "₹329",
        "food_rating_count": "786 votes",
        "food_image_url": "http",
        "food_description": "Chicken Biryani (Serves 2) + Egg + Onion raitha + Brinjal Curry + ... read more"
      },
      "Chicken Bucket Biryani Combo [Serves 5]": {
        "food_price": "₹1800",
        "food_rating_count": "19 votes",
        "food_image_url": "http",
        "food_description": "Chicken Bucket Biryani [Serves 4-5]+chicken [8 pieces]+Chicken 65 [6 pieces]+5 Boiled egg+ Brinjal ... read more"
      },
      "Chicken Bucket Biryani Combo [Serves 8-9]": {
        "food_price": "₹2700",
        "food_description": "Chicken Bucket Biryani [Serves 8-9]+Chicken [16 pieces]+Chicken 65 [12 pieces]+10 Boiled egg+ Brinjal ... read more"
      },
      "Chicken 65": {
        "food_price": "₹299",
        "food_rating_count": "120 votes",
        "food_image_url": "http",
        "food_description": "Spicy deep fried chicken chunks prepared with green chillies, yogurt, curry leaves, salt ... read more"
      },
      "Boneless Chicken 65": {
        "food_price": "₹310",
        "food_rating_count": "20 votes",
        "food_description": "Spicy deep fried boneless chicken prepared with green chillies, yogurt, curry leaves, salt ... read more"
      },
      "Chicken Fry": {
        "food_price": "₹340",
        "food_image_url": "http"
      },
      "Pepper Chicken": {
        "food_price": "₹340",
        "food_rating_count": "34 votes",
        "food_image_url": "http",
        "food_description": "Marinated chicken cooked in a gravy from onions, green chillies, curry leaves, masala ... read more"
      },
      "Mutton Fry (4 Pcs)": {
        "food_price": "₹360"
      },
      "Mutton Pepper Fry": {
        "food_price": "₹370",
        "food_rating_count": "16 votes"
      },
      "Prawns Fry": {
        "food_price": "₹350",
        "food_rating_count": "16 votes",
        "food_image_url": "http"
      },
      "Prawns 65 (Dry)": {
        "food_price": "₹310",
        "food_rating_count": "12 votes",
        "food_image_url": "http"
      },
      "Prawns Pepper Fry": {
        "food_price": "₹360",
        "food_rating_count": "9 votes",
        "food_image_url": "http"
      },
      "Kaada Fry": {
        "food_price": "₹250",
        "food_description": "[Quail]"
      },
      "Kaada Pepper Fry": {
        "food_price": "₹250",
        "food_description": "[Quail]"
      },
      "Kaada 65": {
        "food_price": "₹230",
        "food_description": "[Quail]"
      },
      "Chicken Manchurian": {
        "food_price": "₹340"
      },
      "Ginger Chicken": {
        "food_price": "₹340"
      },
      "Garlic Chicken": {
        "food_price": "₹340"
      },
      "Chilli Chicken": {
        "food_price": "₹340",
        "food_rating_count": "39 votes",
        "food_image_url": "http",
        "food_description": "A popular Indo Chinese appetizer made from boneless cubes marinated in soya sauce, ... read more"
      },
      "Prawns Manchurian": {
        "food_price": "₹350",
        "food_rating_count": "5 votes",
        "food_image_url": "http"
      },
      "Chilli Prawns": {
        "food_price": "₹350",
        "food_image_url": "http"
      },
      "Paneer Chilli Dry": {
        "food_price": "₹310",
        "food_rating_count": "9 votes"
      },
      "Paneer 65": {
        "food_price": "₹270",
        "food_image_url": "http"
      },
      "Kadai Paneer": {
        "food_price": "₹260",
        "food_rating_count": "9 votes",
        "food_image_url": "http"
      },
      "Mushroom 65": {
        "food_price": "₹250",
        "food_image_url": "http"
      },
      "Mushroom Masala": {
        "food_price": "₹260",
        "food_image_url": "http"
      },
      "Mushroom Manchurian": {
        "food_price": "₹260",
        "food_rating_count": "5 votes",
        "food_description": "Kindly Note in customer instruction you want Dry [or] Gravy"
      },
      "Mushroom Chilli": {
        "food_price": "₹260"
      },
      "Veg Fried Rice": {
        "food_price": "₹230",
        "food_rating_count": "40 votes",
        "food_image_url": "http"
      },
      "Mushroom Fried Rice": {
        "food_price": "₹230",
        "food_rating_count": "26 votes",
        "food_image_url": "http",
        "food_description": "A popular Indo Chinese dish made from roasted mushrooms with garlic, olive oil ... read more"
      },
      "Veg Noodles": {
        "food_price": "₹220",
        "food_rating_count": "8 votes",
        "food_image_url": "http"
      },
      "Egg Fried Rice": {
        "food_price": "₹250",
        "food_rating_count": "26 votes",
        "food_image_url": "http",
        "food_description": "A popular Indo Chinese dish made from scarmbled eggs and fragrant rice."
      },
      "Egg Noodles": {
        "food_price": "₹250"
      },
      "Chicken Fried Rice": {
        "food_price": "₹270",
        "food_rating_count": "156 votes",
        "food_description": "A popular Indo Chinese dish made from tender chunks of chicken and soya ... read more"
      },
      "Chicken Noodles": {
        "food_price": "₹270",
        "food_rating_count": "48 votes",
        "food_image_url": "http"
      },
      "Mutton Fried Rice": {
        "food_price": "₹310",
        "food_rating_count": "12 votes",
        "food_image_url": "http"
      },
      "Mutton Noodles": {
        "food_price": "₹290",
        "food_image_url": "http"
      },
      "Prawns Fried Rice": {
        "food_price": "₹280",
        "food_rating_count": "18 votes",
        "food_image_url": "http",
        "food_description": "A popular Indo Chinese dish made from prawns and cooked rice tossed in ... read more"
      },
      "Prawns Noodles": {
        "food_price": "₹290",
        "food_image_url": "http"
      },
      "Mixed Fried Rice": {
        "food_price": "₹310",
        "food_rating_count": "18 votes",
        "food_description": "Contains egg, chicken & prawns."
      },
      "Mixed Noodles": {
        "food_price": "₹310",
        "food_description": "Contains egg, chicken & prawns."
      }
    }
  }
