from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Yoga & Meditation Data
yoga_asanas = {
    "Vata": [
        {
            "name": "Tree Pose",
            "duration": {"value": 5, "unit": "minutes"},
            "time": "Morning",
            "image": "https://i.ibb.co/BHGx9Zdk/Whats-App-Image-2025-05-10-at-01-27-08-ff91fa2f.jpg ",
            "video": "https://www.youtube.com/watch?v=yVE4XXFFO70&utm_source=chatgpt.com"

        },
        {
            "name": "Warrior Pose",
            "duration": {"value": 7, "unit": "minutes"},
            "time": "Morning",
            "image": "https://i.ibb.co/MxHDjpdq/Whats-App-Image-2025-05-10-at-01-27-21-93386725.jpg",
            "video": "https://www.youtube.com/watch?v=5rT--p_cLOc&utm_source=chatgpt.com"
        },
        {
            "name": "Downward Dog",
            "duration": {"value": 6, "unit": "minutes"},
            "time": "Evening",
            "image":"https://i.ibb.co/jvFKmG3R/Whats-App-Image-2025-05-10-at-01-27-36-38eca4b3.jpg",
            "video":"https://www.youtube.com/watch?v=j97SSGsnCAQ&utm_source=chatgpt.com"
        },
        {
            "name": "Seated Forward Bend",
            "duration": {"value": 8, "unit": "minutes"},
            "time": "Evening",
            "image":"https://i.ibb.co/VYXjgS7M/Whats-App-Image-2025-05-10-at-01-31-15-ad36a53d.jpg",
            "video":"https://www.youtube.com/watch?v=W8uyYErso_0&utm_source=chatgpt.com"
        }
    ],
    "Pitta": [
        {
            "name": "Child's Pose",
            "duration": {"value": 6, "unit": "minutes"},
            "time": "Evening",
            "video":"https://www.youtube.com/watch?v=eqVMAPM00DM&utm_source=chatgpt.com",
            "image":"https://i.ibb.co/XkGKJ9nK/Whats-App-Image-2025-05-10-at-23-38-35-f35606a4.jpg"
        },
        {
            "name": "Triangle Pose",
            "duration": {"value": 7, "unit": "minutes"},
            "time": "Morning",
            "video":"https://www.youtube.com/watch?v=upFYlxZHif0&utm_source=chatgpt.com",
            "image":"https://i.ibb.co/G4hLLXZG/Whats-App-Image-2025-05-10-at-23-39-10-7a8895eb.jpg"
        },
        {
            "name": "Bridge Pose",
            "duration": {"value": 8, "unit": "minutes"},
            "time": "Evening",
            "video":"https://www.youtube.com/watch?v=NnbvPeAIhmA&utm_source=chatgpt.com",
            "image":"https://i.ibb.co/1prHzc8/Whats-App-Image-2025-05-10-at-23-39-41-8f8edc7f.jpg"
        },
        {
            "name": "Camel Pose",
            "duration": {"value": 5, "unit": "minutes"},
            "time": "Morning",
            "video":"https://www.youtube.com/watch?v=AigVwIFvmAQ&utm_source=chatgpt.com",
            "image":"https://i.ibb.co/nq7j5dss/Whats-App-Image-2025-05-10-at-23-57-55-ff577a32.jpg"
        }
    ],
    "Kapha": [
        {
            "name": "Sun Salutation",
            "duration": {"value": 10, "unit": "minutes"},
            "time": "Morning",
            "video":"https://www.youtube.com/watch?v=73sjOu0g58M&utm_source=chatgpt.com",
            "image":"https://i.ibb.co/JFwqdGFC/Whats-App-Image-2025-05-10-at-23-58-48-d6815772.jpg"
           
        },
        {
            "name": "Bow Pose",
            "duration": {"value": 7, "unit": "minutes"},
            "time": "Afternoon",
            "video":"https://www.youtube.com/watch?v=CZGtSaOvb50&utm_source=chatgpt.com",
            "image":"https://i.ibb.co/VpwhKh3t/Whats-App-Image-2025-05-11-at-00-17-55-f354731c.jpg"
        },
        {
            "name": "Cobra Pose",
            "duration": {"value": 6, "unit": "minutes"},
            "time": "Morning",
            "video":"https://www.youtube.com/watch?v=n6jrC6WeF84&utm_source=chatgpt.com",
            "image":"https://i.ibb.co/YFYvwtyF/Whats-App-Image-2025-05-11-at-00-21-33-1c2821e8.jpg"

        },
        {
            "name": "Lotus Pose",
            "duration": {"value": 5, "unit": "minutes"},
            "time": "Evening",
            "video":"https://www.youtube.com/watch?v=y9u3MwkuHYQ&utm_source=chatgpt.com",
            "image":"https://i.ibb.co/6RQ8LrFw/Whats-App-Image-2025-05-11-at-00-19-55-1f242942.jpg"
        }
    ]
}

meditation_data = {
    "Vata": {
        "description": "Grounding meditation with body awareness.",
        "duration": {"value": 15, "unit": "minutes"},
        "image" : "https://i.ibb.co/ZRrz4stw/Whats-App-Image-2025-05-11-at-13-42-37-9e008a5f.jpg"
    },
    "Pitta": {
        "description": "Cooling meditation with breathwork.",
        "duration": {"value": 12, "unit": "minutes"},
        "image": "https://i.ibb.co/LzSkTzDp/Whats-App-Image-2025-05-11-at-13-42-47-87dab2eb.jpg"
    },
    "Kapha": {
        "description": "Energizing meditation with movement.",
        "duration": {"value": 10, "unit": "minutes"},
        "image":"https://i.ibb.co/3mL0HkXx/Whats-App-Image-2025-05-11-at-13-42-59-8c1b22c7.jpg"
    }
}

# Dosha insights and qualities
dosha_insights = {
    "Vata": "Vata types are creative, energetic, and quick thinkers but may experience anxiety, dryness, and irregular routines. Grounding routines, warm foods, and regular schedules help balance Vata.",
    "Pitta": "Pitta types are focused, intense, and intelligent, but may struggle with anger or overheating. Cooling foods, calm environments, and relaxation help balance Pitta.",
    "Kapha": "Kapha types are calm, compassionate, and strong but may feel lazy or gain weight easily. Stimulating routines, light foods, and energetic exercise balance Kapha."
}

dosha_qualities = {
    "Vata": ["Dry", "Cold", "Light", "Irregular", "Mobile", "Creative"],
    "Pitta": ["Hot", "Sharp", "Intense", "Ambitious", "Focused", "Fiery"],
    "Kapha": ["Heavy", "Stable", "Slow", "Cool", "Loyal", "Calm"]
}

# Diet section
diet_data = {
    "Vata": {
        "prefer": ["Warm soups", "Cooked vegetables", "Rice", "Ghee", "Oats"],
        "avoid": ["Raw foods", "Cold drinks", "Caffeine", "Dry snacks"],
        "insight": "Vata should prefer grounding, warm, and moist foods to counter dryness and cold.",
        "meals": {
            "breakfast": "Warm oatmeal with ghee and cinnamon",
            "lunch": "Steamed rice with cooked lentils and sautéed veggies",
            "dinner": "Vegetable soup with ghee toast"
        }
    },
    "Pitta": {
        "prefer": ["Coconut", "Cucumber", "Mint", "Sweet fruits", "Milk"],
        "avoid": ["Spicy food", "Alcohol", "Tomatoes", "Onion", "Garlic"],
        "insight": "Pitta benefits from cooling, calming foods to counter internal heat.",
        "meals": {
            "breakfast": "Coconut milk smoothie with banana",
            "lunch": "Mint rice with cucumber raita",
            "dinner": "Sweet potato mash with steamed broccoli"
        }
    },
    "Kapha": {
        "prefer": ["Light soups", "Barley", "Green veggies", "Spices", "Fruits"],
        "avoid": ["Heavy dairy", "Fried food", "Sugar", "Red meat"],
        "insight": "Kapha needs stimulating and light foods to maintain energy and avoid sluggishness.",
        "meals": {
            "breakfast": "Warm herbal tea with barley upma",
            "lunch": "Mixed vegetable stir fry with millet",
            "dinner": "Clear lentil soup with salad"
        }
    }
}

# Dosha detection
def detect_dosha(data):
    vata = pitta = kapha = 0

    frame = data.get('bodyFrame', '').lower()
    skin = data.get('skinType', '').lower()
    hair = data.get('hairType', '').lower()
    digestive = data.get('digestivePattern', '').lower()
    energy = data.get('energy', '').lower()
    sleep = data.get('sleep', '').lower()
    emotion = data.get('emotion', '').lower()
    activity = data.get('physicalActivity', '').lower()
    diet = data.get('diet', '').lower()

    if "thin" in frame: vata += 1
    if "medium" in frame: pitta += 1
    if "large" in frame: kapha += 1

    if "dry" in skin: vata += 1
    if "oily" in skin: pitta += 1
    if "smooth" in skin: kapha += 1

    if "soft" in hair or "fine" in hair: vata += 1
    if "greying" in hair or "thin" in hair: pitta += 1
    if "thick" in hair: kapha += 1

    if "irregular" in digestive: vata += 1
    if "fast" in digestive or "acid" in digestive: pitta += 1
    if "slow" in digestive: kapha += 1

    if "drains" in energy or "erratic" in energy: vata += 1
    if "intense" in energy: pitta += 1
    if "stable" in energy: kapha += 1

    if "light" in sleep or "interrupted" in sleep: vata += 1
    if "short" in sleep: pitta += 1
    if "deep" in sleep or "long" in sleep: kapha += 1

    if "anxious" in emotion or "overwhelmed" in emotion: vata += 1
    if "angry" in emotion or "irritable" in emotion: pitta += 1
    if "calm" in emotion or "lazy" in emotion: kapha += 1

    if "intense" in activity or "regular" in activity: pitta += 1
    if "irregular" in activity: vata += 1
    if "less" in activity or "none" in activity: kapha += 1

    if "light" in diet: vata += 1
    if "spicy" in diet or "rich" in diet: pitta += 1
    if "heavy" in diet: kapha += 1

    scores = {"Vata": vata, "Pitta": pitta, "Kapha": kapha}
    dominant = max(scores, key=scores.get)

    return {
        "dosha": dominant,
        "score": scores,
        "userInfo": {
            "ageGroup": data.get('ageGroup', ''),
            "sex": data.get('sex', ''),
            "city": data.get('city', ''),
            "country": data.get('country', ''),
            "goal": data.get('mainHealthGoal', ''),
            "condition": data.get('medicalCondition', ''),
            "allergies": data.get('foodAllergies', [])
        }
    }

@app.route('/log_data', methods=['POST'])
def analyze_dosha():
    data = request.get_json()
    result = detect_dosha(data)
    dosha = result["dosha"]
    allergies = result["userInfo"].get("allergies", [])

    # Filter diet suggestions based on allergies
    diet = diet_data[dosha].copy()
    if allergies:
        diet["prefer"] = [food for food in diet["prefer"] if food not in allergies]

    return jsonify({
        "dosha": dosha,
        "score": result["score"],
        "qualities": dosha_qualities[dosha],
        "insight": dosha_insights[dosha],
        "yoga": yoga_asanas[dosha],
        "meditation": meditation_data[dosha],
        "diet": diet,
        "userInfo": result["userInfo"]
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
