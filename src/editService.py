from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Load OpenAI API key
openai.api_key = "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"

@app.route('/edit')
def edit():
    prompt = request.args.get('prompt')
    if not prompt:
        return jsonify(error="Prompt parameter is missing"), 400

    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5
        )
        return jsonify(response=response.choices[0].text.strip())
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)