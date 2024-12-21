async function generateMealPlan(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    
    const payload = {
        dietary_restrictions: formData.getAll('dietary-restrictions'),
        calorie_goal: parseInt(formData.get('calorie-goal')),
        cuisine_preference: formData.get('cuisine') || null
    };

    const response = await fetch('/meal-plan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    });

    const result = await response.json();
    document.getElementById('meal-plan-result').innerText = JSON.stringify(result, null, 2);
}

async function findSubstitutes() {
    const ingredient = document.getElementById('ingredient-input').value;
    const response = await fetch(`/ingredient-substitutes/${ingredient}`);
    const result = await response.json();
    document.getElementById('substitutes-result').innerText = JSON.stringify(result, null, 2);
}

document.getElementById('meal-plan-form').addEventListener('submit', generateMealPlan);