# Zomato Restaurant Data Harvesting

main.py file contain code which uses selenium webdriver & BeautifulSoup to scrap restaurant data from Zomoto website in Json,

https://raw.githubusercontent.com/VISHNU-ARAVIND-99/zomoto_web_scraping/main/output.json

I scraped 1166 restaurant data u can see in above link.


## Following is the example data of one restaurant :

    {"restaurant name": "KFC",
    "restaurant_zomoto_link": "https://www.zomato.com/chennai/kfc-2-park-town/",
    "description": "Burger, Fast Food",
    "location": "Park Town, Chennai",
    "opening_time": "11am – 11pm (Today)",
    "phone_num": "+918042754444",
    "location_google_map_link": "https://www.google.com/maps/dir/?api=1&destination=13.0836800000,80.2705700000",
    "location_address": "55, Ground Floor, Periyamet, Sydenhams Road, Park Town, Chennai",
    "dining_rating": "3.7",
    "delivery_rating": "3.8",
    "dining_rating_count": "20",
    "delivery_rating_count": "1,134",
    "food_item_list": {
      "Chicken Chizza": {
        "food_price": "₹319.05",
        "food_rating_count": "24 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/210/5108c304c25e2360d28588a461e1f210.jpeg",
        "food_description": "Crunchy chicken topped with cheese, spicy sauce, veggies & herbs. All-chicken-no-crust pizza! [Serves ... read more"
      },
      "Chicken Chizza & Wings Meal": {
        "food_price": "₹459.05",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/5ad/120374790af673aae76c5a5d883d45ad.jpeg",
        "food_description": "All-chicken-no-crust Chizza, 2 Pc Hot Wings and a Pepsi PET 475ml at a ... read more"
      },
      "Duo Chicken Chizza": {
        "food_price": "₹628.57",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/7f5/302d1fbc468a89dbc497f3181827a7f5.jpeg",
        "food_description": "2 Crunchy all-chicken-no-crust Chizza topped with cheese, spicy sauce, veggies & herbs [Serves ... read more"
      },
      "Chicken Chizza & Pepsi Combo": {
        "food_price": "₹376.19",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/2ce/aa3caff35ff99fab3dadcd1121a962ce.jpeg",
        "food_description": "Crunchy all-chicken-no-crust Chizza served with Pepsi PET 475ml [Serves 1]"
      },
      "Chicken Chizza & Dessert Meal": {
        "food_price": "₹468.57",
        "food_description": "All-chicken-no-crust Chizza, Choco Lava Cake and a Pepsi PET 475ml at a deal ... read more"
      },
      "Zinger Pro Burger & Popcorn Meal": {
        "food_price": "₹459.05",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/b6c/9b153dffd3829fb695a66e4fd7182b6c.jpeg",
        "food_description": "New Zinger Pro premium Burger with Medium Popcorn and Pepsi PET 475ml at ... read more"
      },
      "Zinger Pro Burger": {
        "food_price": "₹239.05",
        "food_rating_count": "20 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/6c8/36901b422d759c19c2799c10eeb416c8.jpeg",
        "food_description": "New premium zinger with crunchy zinger fillet,cheese,lettuce,tomatoes,sauce in sesame bun!"
      },
      "Zinger Pro Burger & Chicken Meal": {
        "food_price": "₹399.05",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/521/6bafd5f307841d1025401757c7be3521.jpeg",
        "food_description": "New Zinger Pro premium Burger with 1 Pc Hot & Crispy and Pepsi ... read more"
      },
      "Chicken Burger Buddy Meal": {
        "food_price": "₹528.57",
        "food_rating_count": "8 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/5cd/8f9137a6bae94a4d61fcc4fa1c3c15cd.jpeg",
        "food_description": "Save Rs. 40 & Share 2 Classic Chicken Zinger Burgers & a Medium ... read more"
      },
      "Mixed Chicken Zinger Burger Doubles": {
        "food_price": "₹368.57",
        "food_rating_count": "44 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/b46/dd434d7cd80de42b3d04cb979aeacb46.jpeg",
        "food_description": "Save Rs.41 on Best-seller combo of classic chicken Zinger & Tandoori zinger burgers"
      },
      "Chicken Zinger Burger - Classic with Cheese": {
        "food_price": "₹224.05",
        "food_rating_count": "8 votes",
        "food_description": "Signature burger with a crunchy chicken fillet, cheese slice, veggies & a delicious ... read more"
      },
      "Chicken Zinger Burger - Tandoori with Cheese": {
        "food_price": "₹233.57",
        "food_rating_count": "8 votes",
        "food_description": "Chicken zinger with delicious tandoori sauce & cheese slice"
      },
      "Veg Zinger Burger with Cheese": {
        "food_price": "₹213.57",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/fed/6d8c645fcd7d5368741ccc61933fafed.jpeg",
        "food_description": "Signature veg burger with crispy patties, cheese slice, veggies & a tangy sauce"
      },
      "Chicken Zinger Burger - Classic": {
        "food_price": "₹199.05",
        "food_rating_count": "136 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/72b/d5bc5b32dd177f5f207cad66556a572b.jpeg",
        "food_description": "Signature burger made with a crunchy chicken fillet, veggies & a delicious mayo ... read more"
      },
      "Veg Zinger Burger": {
        "food_price": "₹188.57",
        "food_rating_count": "6 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/165/a403a55dc5b74cc6acfcfa755f30c165.jpeg",
        "food_description": "Signature veg burger with crispy patties, veggies & a tangy sauce"
      },
      "Chicken Zinger Burger - Tandoori": {
        "food_price": "₹208.57",
        "food_rating_count": "35 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/e97/af3699168db40a2dbadc372d87338e97.jpeg",
        "food_description": "Chicken zinger with a  delicious tandoori sauce"
      },
      "2 X Veg Krisper Burgers": {
        "food_price": "₹179.05",
        "food_rating_count": "9 votes",
        "food_description": "2 Delicious veg value burgers - at a deal price"
      },
      "2 X Chicken Krisper Burgers": {
        "food_price": "₹248.57",
        "food_rating_count": "49 votes",
        "food_description": "2 Delicious chicken value burgers - at a deal price"
      },
      "Peri Peri Chicken 5 Leg Piece Meal": {
        "food_price": "₹648.57",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/bfc/41d33f8aaf13fe78fa49141e53faabfc.jpeg",
        "food_description": "Leg before any wicket! Save Rs. 148 on 5 Spicy Peri Peri Leg ... read more"
      },
      "Peri Peri 10 Pc Chicken Strips & 2 Dips": {
        "food_price": "₹499.05",
        "food_rating_count": "15 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/948/a0feef07b2a9d72ba02f4a7d53e46948.jpeg",
        "food_description": "Howzatt Deal!! Save 24% with the indulging 10 Piece Peri Peri Boneless Strips ... read more"
      },
      "Peri Peri Chicken 5 Leg Piece & 2 Dips": {
        "food_price": "₹519.05",
        "food_rating_count": "15 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/390/180441e941f23ad56ace5f6c9a7a8390.jpeg",
        "food_description": "Save Rs 120 on 5 Spicy Peri Peri Leg Pieces, paired with 2 ... read more"
      },
      "Peri Peri Chicken 10 Leg Pc & 4 Dips": {
        "food_price": "₹948.57",
        "food_description": "Save Rs. 334 on 10 Spicy Peri Peri Leg Pieces & 4 Dips ... read more"
      },
      "Peri Peri chicken strips - 6 Pc": {
        "food_price": "₹299.05",
        "food_rating_count": "42 votes",
        "food_description": "Save 16% with on savouring 6 Spicy Peri Peri chicken boneless strips [serves ... read more"
      },
      "House Party Chicken Combo": {
        "food_price": "₹819.05",
        "food_description": "Save Rs. 263  with the ultimate party combo of 4pc Hot & ... read more"
      },
      "Chicken Biryani Combo for Two": {
        "food_price": "₹795.24",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/bfb/a02277f3e76f17f907a0ea399538ebfb.jpeg",
        "food_description": "Weekends are for Biryani! Enjoy this new combo of 2 Chicken Popcorn Biryani ... read more"
      },
      "Chick n Dip Combo": {
        "food_price": "₹719.05",
        "food_description": "Save Rs. 249 with this dipping combo of 10pc chicken peri peri boneless ... read more"
      },
      "Zinger Burger & Chicken Combo": {
        "food_price": "₹524.76",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/5e2/6577ab2169912620f0906930a496c5e2.jpeg",
        "food_description": "Weekend mood set with Chicken Zinger Burger, Medium Chicken Popcorn, 4 chicken Hot ... read more"
      },
      "Chicken Bucket for Two": {
        "food_price": "₹599.05",
        "food_description": "Flat Rs. 115 off with this variety combo of 2pc Hot & Crispy ... read more"
      },
      "Chicken Krisper Burger Combo": {
        "food_price": "₹539.05",
        "food_rating_count": "9 votes",
        "food_description": "Save Rs. 57 on Deal combo of 2 chicken value burgers, 2 pc ... read more"
      },
      "Chicken Mingles Bucket Meal": {
        "food_price": "₹499.05",
        "food_rating_count": "6 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/41e/ebae1c0011528ae0297182f4f99c141e.jpeg",
        "food_description": "Save Rs. 63 on this crowd favorite combo of 4 Hot Wings, 2 ... read more"
      },
      "Chicken Solo Feast": {
        "food_price": "₹399.05",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/26d/f69baf2973745c0d9b38f3c06b10d26d.jpeg",
        "food_description": "Treat yourself with 1 Hot & Crispy chicken, 2 chicken Strips, 2 chicken ... read more"
      },
      "Chicken Mingles Bucket": {
        "food_price": "₹379.05",
        "food_rating_count": "36 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/aaf/722ea4b11a44b71502a9cfd83e031aaf.jpeg",
        "food_description": "Save Rs. 26 and Mingle with 4 Chicken Hot Wings, 2 Chicken peri ... read more"
      },
      "Chicken & French Fries Bucket": {
        "food_price": "₹299.05",
        "food_rating_count": "6 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/ac3/43bfbb06b390db918d165ff84a289ac3.jpeg",
        "food_description": "Crowd-favorite combo of 2pc Hot & Crispy Chicken with Medium French Fries"
      },
      "Chicken Popcorn & French Fries Bucket": {
        "food_price": "₹319.05",
        "food_rating_count": "15 votes",
        "food_description": "Large Chicken Popcorn with Med French Fries - at a deal price"
      },
      "2 X Veg Krispers Burger Meal": {
        "food_price": "₹288.57",
        "food_description": "Save Rs. 49 with 2 veg value burgers, crispy Medium French Fries & ... read more"
      },
      "All in One Chicken Bucket": {
        "food_price": "₹548.57",
        "food_rating_count": "13 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/06f/31f899d11feb6a4bc6b3af7815e0f06f.jpeg",
        "food_description": "Save 24% with variety bucket of 1 Leg Pc, 1 Hot & Crispy, ... read more"
      },
      "Ultimate Savings Chicken Bucket": {
        "food_price": "₹699.05",
        "food_rating_count": "70 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/12a/6ed1175bffa256e8470995657b08f12a.jpeg",
        "food_description": "Savings of 35% on signature bucket of 4pc Hot & crispy chicken, 6 ... read more"
      },
      "Stay Home Chicken Bucket": {
        "food_price": "₹799.05",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/a85/baa2a00813d69c9a0a8451c2962eba85.jpeg",
        "food_description": "Save 24% & enjoy 4pc Hot & Crispy Chicken, 4 Hot Wings, 6 ... read more"
      },
      "Big 12 - Chicken Bucket": {
        "food_price": "₹748.57",
        "food_rating_count": "20 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/1b2/60312a35614a78481cea0e8fe31121b2.jpeg",
        "food_description": "Save 26% on 6pc Hot & Crispy Chicken, 6 Hot Wings & 2 ... read more"
      },
      "Big 8 - Chicken Bucket": {
        "food_price": "₹699.05",
        "food_description": "Save 27% on this variety bucket of 4pc Hot & Crispy chicken & ... read more"
      },
      "Classic Chicken Biryani Combo": {
        "food_price": "₹740",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/9e9/6972db6070be7244eb3421319a4219e9.jpeg",
        "food_description": "Large Biryani rice with 2 Hot & Crispy, 2 Gravies, 4 Strips & ... read more"
      },
      "Smoky Red Grilled Chicken Biryani Combo": {
        "food_price": "₹740",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/9c6/8f9ce80dfcaaaca5aee2e9861c68e9c6.jpeg",
        "food_description": "Large Biryani rice with 2 Smoky Red, 2 Gravies, Med Popcorn & 1 ... read more"
      },
      "Classic Chicken Biryani Bucket-Large": {
        "food_price": "₹475.24",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/e96/395b380ddf1a0e35c82018c63c03ee96.jpeg",
        "food_description": "Large portions of Biryani rice served with 2 pc Hot & Crispy Chicken ... read more"
      },
      "Popcorn Chicken Biryani Bucket -Large": {
        "food_price": "₹475.24",
        "food_rating_count": "5 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/052/73034f2652a5be5bfbcee654829a3052.jpeg",
        "food_description": "Large portions of Biryani rice served with Chicken Popcorn & 2 Gravies [serves ... read more"
      },
      "Smoky Red Grilled Chicken Biryani Bucket - Large": {
        "food_price": "₹475.24",
        "food_description": "Large portions of Biryani rice served with 2 pc Smoky Red Chicken & ... read more"
      },
      "Chicken Strips & Rice Combo": {
        "food_price": "₹359.05",
        "food_description": "Combo of  4 chicken peri peri boneless strips, 1 Dips (20gm), flavorful ... read more"
      },
      "Classic Chicken Biryani Bucket": {
        "food_price": "₹229.52",
        "food_rating_count": "5 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/e84/0c3aa10ef82ac87317bf66b0bcec9e84.jpeg",
        "food_description": "Hyderabadi style Biryani rice served with 1 pc Hot & Crispy & Spicy ... read more"
      },
      "Popcorn Chicken Biryani Bucket": {
        "food_price": "₹229.52",
        "food_rating_count": "21 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/bdd/725162deeb004cc683f1af5dd3a72bdd.jpeg",
        "food_description": "Hyderabadi style Biryani rice served with Popcorn & Spicy Gravy [serves 1]"
      },
      "Smoky Red Grilled Chicken Biryani Bucket": {
        "food_price": "₹229.52",
        "food_rating_count": "8 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/7b7/0616a916c0dec5e69730cf0ae539f7b7.jpeg",
        "food_description": "Hyderabadi style Biryani rice served with 1 pc Smoky Red & Spicy Gravy ... read more"
      },
      "Veg Biryani Bucket": {
        "food_price": "₹199.05",
        "food_rating_count": "7 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/651/b4ed59ec4791ecd6e9aab782944e5651.jpeg",
        "food_description": "Hyderabadi style Biryani rice served with Veg Patty & Spicy Gravy [serves 1]"
      },
      "Double Chicken Roll Meal for 2": {
        "food_price": "₹548.57",
        "food_description": "Deal combo of 2 Classic Chicken Rolls, Large Fries, 2 Dips & Pepsi ... read more"
      },
      "Classic Chicken Roll Meal for 2": {
        "food_price": "₹479.05",
        "food_description": "Deal combo of 2 Double Chicken Rolls, Large Fries, 2 Dips & Pepsi ... read more"
      },
      "Double Chicken Roll Meal for 1": {
        "food_price": "₹379.05",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/e4b/0397fd0e70e0aa7d774cc0213664de4b.jpeg",
        "food_description": "Deal combo of 1 Double Chicken Roll, Large Fries, 2 Dips & Pepsi ... read more"
      },
      "Classic Chicken Roll Meal for 1": {
        "food_price": "₹339.05",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/e75/b3db0c5fa1ffe9b2726a757ce00a6e75.jpeg",
        "food_description": "Deal combo of 1 Classic Chicken Roll, Large Fries, 2 Dips & Pepsi ... read more"
      },
      "2 Double Chicken Rolls": {
        "food_price": "₹328.57",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/d32/b881c8de97cefa72c822926e43a38d32.jpeg",
        "food_description": "Double the fun with 2 Double Chicken Rolls [serves 2]"
      },
      "2 Classic Chicken Rolls": {
        "food_price": "₹228.57",
        "food_rating_count": "10 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/dab/9c67bdcd5218f5b53a858f4665ad0dab.jpeg",
        "food_description": "Double the fun with 2 Classic Chicken Rolls [serves 2]"
      },
      "Double Chicken Roll & Pepsi Combo": {
        "food_price": "₹225.71",
        "food_description": "Our new Double Chicken Roll served with Pepsi 475ml [serves 1]"
      },
      "Classic Chicken Roll & Pepsi Combo": {
        "food_price": "₹176.19",
        "food_rating_count": "5 votes",
        "food_description": "Our new Classic Chicken Roll served with Pepsi 475ml [serves 1]"
      },
      "Double Chicken Roll": {
        "food_price": "₹168.57",
        "food_rating_count": "15 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/847/ebcda29a62123bbf8bb8a33bbe2ab847.jpeg",
        "food_description": "KFC's take on the street style roll with double chicken strips, onions & ... read more"
      },
      "Classic Chicken Roll": {
        "food_price": "₹119.05",
        "food_rating_count": "40 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/cba/ebd8e706049e4fd5ca79ecf708f8ecba.jpeg",
        "food_description": "KFC's take on the street style roll with single chicken strip, onions & ... read more"
      },
      "Chicken Longer Burger & 2 Strips Combo": {
        "food_price": "₹219.05",
        "food_rating_count": "49 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/a4b/e344aa3aac91a825e9d0d0e3f60eda4b.jpeg",
        "food_description": "Longgg burger with crunchy chicken, onions & a punchy sauce , served with ... read more"
      },
      "Chicken Popcorn - Regular": {
        "food_price": "₹115.24",
        "food_rating_count": "54 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/838/4dbe2c53e785fc137b6301fbc21a8838.jpeg",
        "food_description": "Signature bite-sized boneless chicken, with special spices"
      },
      "2 X VegRoll": {
        "food_price": "₹228.57",
        "food_description": "Try the amazing Veg Roll [2 units of Veg Roll]"
      },
      "Veg Roll Meal": {
        "food_price": "₹399.05",
        "food_description": "Deal meal of 2 Veg Rolls, Large Fries and a Pepsi PET 475ml ... read more"
      },
      "2 X Veg Longer Burger": {
        "food_price": "₹198.10",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/d97/866ef0fcc37944827cf419f6d9783d97.jpeg",
        "food_description": "The really long burger with Veg Patty, Onion, Lettuce and two sauces"
      },
      "Hot & Crispy Chicken - 8 pcs": {
        "food_price": "₹768.57",
        "food_rating_count": "13 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/054/7c1c9c67d06e7d1b765096abc58f2054.jpeg",
        "food_description": "Save Rs. 182 & get 8pc signature Hot & crispy chicken [serves 3-4]"
      },
      "Hot & Crispy Chicken -6pc": {
        "food_price": "₹628.57",
        "food_rating_count": "8 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/230/efb7c1c50bdd20ba436ae281fce0b230.jpeg",
        "food_description": "Flat 10% off on 6pc signature Hot & crispy chicken [serves 2-3]"
      },
      "Hot & Crispy Chicken-4pc": {
        "food_price": "₹428.57",
        "food_rating_count": "32 votes",
        "food_description": "Save Rs. 34 on 4 pc of signature Hot & Crispy Chicken at ... read more"
      },
      "Hot & Crispy Chicken -2pc": {
        "food_price": "₹229.52",
        "food_rating_count": "53 votes",
        "food_description": "Signature Hot & crispy chicken"
      },
      "Hot Chicken Wings - 4pc": {
        "food_price": "₹179.05",
        "food_rating_count": "93 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/479/6e215d110f00aba3c59ce6e67d78c479.jpeg",
        "food_description": "Seasoned, signature KFC chicken wings"
      },
      "Hot & Crispy Chicken-1pc": {
        "food_price": "₹115.24",
        "food_rating_count": "8 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/487/ef114cc07ccb43adc50b76a31ed4c487.jpeg",
        "food_description": "Signature Hot & crispy chicken"
      },
      "Chicken Popcorn - Large": {
        "food_price": "₹248.57",
        "food_rating_count": "96 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/878/eedc20585107cbdcf31aa451344b9878.jpeg",
        "food_description": "Signature bite-sized boneless chicken, with special spices"
      },
      "Chicken Popcorn - Medium": {
        "food_price": "₹168.57",
        "food_rating_count": "101 votes",
        "food_image_url": "https://b.zmtcdn.com/data/dish_photos/d79/1bc82946c1c0bebdc084f6a665338d79.jpeg",
        "food_description": "Signature bite-sized boneless chicken, with special spices"
      },
      "Smoky Red Grilled Chicken - 5 pc": {
        "food_price": "₹528.57",
        "food_rating_count": "8 votes",
        "food_description": "Flat 20% off on 5pc Smoky red grilled chicken [serves 2]"
      },
      "Smoky Red Grilled Chicken - 2 pc": {
        "food_price": "₹248.57",
        "food_rating_count": "5 votes",
        "food_description": "Spicy, red, grilled chicken"
      },
      "Smoky Red Grilled Chicken - 1 pc": {
        "food_price": "₹124.76",
        "food_rating_count": "7 votes",
        "food_description": "Spicy, red, grilled chicken"
      },
      "Peri Peri chicken strips - 3 pc": {
        "food_price": "₹179.05",
        "food_rating_count": "10 votes",
        "food_description": "3 Pieces Spicy Peri Peri chicken boneless strips"
      },
      "2 pc Veg Patty": {
        "food_price": "₹155.24",
        "food_description": "Delicious, crispy, veg add-on"
      },
      "Spicy Mix French Fries - Large": {
        "food_price": "₹139.05",
        "food_rating_count": "12 votes",
        "food_description": "Crispy french fries with a spicy chilli lime sprinkle"
      },
      "French Fries - Large": {
        "food_price": "₹119.05",
        "food_rating_count": "15 votes",
        "food_description": "Jazz up your meal with crispy large fries!"
      },
      "Spicy Mix French Fries - Medium": {
        "food_price": "₹114.29",
        "food_rating_count": "8 votes",
        "food_description": "Crispy french fries with a spicy chilli lime sprinkle"
      },
      "French Fries - Medium": {
        "food_price": "₹99.05",
        "food_rating_count": "29 votes",
        "food_description": "Jazz up your meal with crispy french fries"
      },
      "Pack of 4 Dips -20gm each": {
        "food_price": "₹109.52",
        "food_rating_count": "5 votes",
        "food_description": "Adding dips is always a good idea! (Save Rs. 5)"
      },
      "Pack of 2 Dips-20gm each": {
        "food_price": "₹57.14",
        "food_rating_count": "10 votes",
        "food_description": "Adding dips is always a good idea!"
      },
      "Tandoori Masala Dip -20gm": {
        "food_price": "₹28.57",
        "food_rating_count": "26 votes",
        "food_description": "Special tandoori flavored dip, to add a twist to your meal!"
      },
      "Chocolate Lava Cake": {
        "food_price": "₹108.57",
        "food_rating_count": "14 votes",
        "food_description": "New Soft Chocolate cake with a gooey center- perfect chocolaty end to every ... read more"
      },
      "Chocolate Mud Pie": {
        "food_price": "₹128.57",
        "food_rating_count": "7 votes",
        "food_description": "Chocolate lovers unite! Say hello to our delicious, new, creamy chocolate & cake ... read more"
      },
      "Coffee Mousse Cake": {
        "food_price": "₹128.57",
        "food_rating_count": "5 votes",
        "food_description": "Coffee, chocolate, cake?what's not to love? Enjoy our delicious, new dessert for those ... read more"
      },
      "Pepsi PET 475ml": {
        "food_price": "₹57.14",
        "food_rating_count": "29 votes",
        "food_description": "Cheers to fizz that makes you Rise Up Baby! Order Pepsi to make ... read more"
      },
      "Pepsi Can 300 ml": {
        "food_price": "₹57.14",
        "food_rating_count": "10 votes",
        "food_description": "Cheers to fizz that makes you Rise Up Baby! Order Pepsi to make ... read more"
      },
      "7UP Can 300 ml": {
        "food_price": "₹57.14",
        "food_rating_count": "8 votes",
        "food_description": "7UP is the ultimate Super-Duper Refresher. Every sip of this crisp lemon flavour ... read more"
      },
      "Pepsi Black Can 300 ml": {
        "food_price": "₹57.14",
        "food_rating_count": "11 votes",
        "food_description": "Enjoy Pepsi Black to make your food rise up to max levels of ... read more"
      },
      "Mirinda Can 300 ml": {
        "food_price": "₹57.14",
        "food_rating_count": "8 votes",
        "food_description": "Great orange taste and sparking bubbles encourage you to be carefree, spontaneous and ... read more"
      }
    }}
  
