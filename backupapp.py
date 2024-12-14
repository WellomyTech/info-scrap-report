from flask import Flask, render_template, request
from openai import OpenAI
import re
import markdown


client = OpenAI(api_key = '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')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    topic_name = request.form['topic_name']
    region = request.form['region']
    first_chat_instructions = "You are an intelligent assistant tasked with analyzing internet activity related to a specific target (person, business, or organization) over the last 7 days. Your goal is to provide a high-level summary and structured output that highlights the most interesting and relevant insights, which will serve as a foundation for creating detailed individual reports."

    first_prompt = f'You are a highly skilled internet analyst tasked with analyzing the online presence and activity of a specific target over the last 7 days. Your job is to produce a detailed, engaging, and structured analysis that provides actionable insights, measurable comparisons, and psychometric trends. This analysis will form the foundation for a comprehensive multi-page report. Target Details: Name: {topic_name}. Region: {region}. Timeframe: Analyze data specifically from the last 7 days. Instructions: Generate 9-11 Unique Topics: Identify at least 9-11 engaging and detailed topics related to the target’s online activity during the specified timeframe. Ensure each topic reflects key developments, public reactions, or noteworthy trends involving the target. The headings must be creative, specific, and newsworthy (e.g., “How [Target Name] Is Transforming Public Perception About [Topic]” or “The Surprising Impact of [Target Name]\'s Recent Actions on [Region]”). Avoid generic or repetitive titles—focus on highlighting unique insights and trends. Content Requirements for Each Topic: Detailed Summary: Provide an in-depth overview of the topic, including relevant activities or developments. Numerical Data: Include specific, measurable metrics such as: Engagement growth rates (e.g., “Engagement increased by 25% compared to last week”). Sentiment distribution percentages (e.g., “40% positive, 35% negative, and 25% neutral”). Platform-specific activity (e.g., “60% of mentions on Twitter, 25% on Facebook, and 15% on Instagram”). Comparative Insights: Highlight how the target’s performance compares to: Previous weeks. Competitors or peers in the same region or field. Broader trends within the industry or region. Psychometric Analysis: Analyze public sentiment and emotional responses: Identify dominant emotions like trust, anger, joy, or fear. Highlight any shifts in sentiment or behavioral trends. Tangible Impacts: Assess the measurable effects of the target’s activities: Changes in public opinion, reputation, or brand perception. Business outcomes, policy shifts, or other significant impacts. Highlight Recurring Themes and Trends: Identify major keywords, hashtags, or recurring phrases associated with the target. Specify which platforms (e.g., Twitter, Facebook, Instagram) saw the most activity for each theme. Predictions for the Future: Based on current data, provide forecasts on how public sentiment, activity levels, or the target’s influence might evolve in the coming weeks. Include data-driven trends and potential scenarios. Special Instructions: Ensure each topic has enough depth and detail to support a multi-page report. The output should include insightful, numerical, and comparative analysis where applicable. Avoid generic or overly broad headings. Focus on creating specific, impactful, and engaging topics tailored to the target. Clearly indicate if certain data points are unavailable, but maintain a comprehensive and analytical approach. Use a professional tone suitable for an executive-level audience. Output Format: Structure the response into a JSON object. For each heading, include subheadings and a detailed summary incorporating all specified data points.Output Format: Provide the output in the following structured format: {{ "target": "[Insert Name]", "entity_type": "[Person/Business/Organization]", "timeframe": "Last 7 days", "content_overview": [ {{ "heading": "[Heading Title 1]", "subheadings": [ "[Subheading 1.1]", "[Subheading 1.2]" ], "summary": "[Brief summary of this section and why it is relevant.]" }}, {{ "heading": "[Heading Title 2]", "subheadings": [ "[Subheading 2.1]", "[Subheading 2.2]" ], "summary": "[Brief summary of this section and why it is relevant.]" }} ] }}'

    response = chat_assist(first_chat_instructions, first_prompt)

    detail_adder_instructions = "Understand the Context: Recognize that the goal is to expand a brief summary, heading, and subheadings into a fully developed section for a report. Each section must provide sufficient depth and insights to stand as a standalone page in a multi-page document. Follow a Logical Structure: For each section: Begin with an introduction that provides context based on the heading and summary. Develop each subheading into a detailed subsection with insights, data, and analysis. Conclude the section with a summary of key takeaways and any broader implications or predictions. Incorporate Data and Analysis: Where applicable: Use quantitative insights from the summary, such as engagement rates, sentiment distribution, or platform metrics. Provide comparative analysis (e.g., with competitors, past trends, or regional benchmarks). Highlight psychometric insights, such as emotional responses or behavioral patterns. Maintain Relevance and Depth: Ensure the content stays relevant to the heading and summary. Expand on the subheadings to add depth, avoiding repetition or generic descriptions. Write Professionally: Use a formal, executive-level tone suitable for a report. Ensure the content flows logically between subsections. Address Missing Data: If specific data points (e.g., numerical metrics or comparative insights) are not available, explicitly state it (e.g., “Detailed data on competitor engagement is unavailable for this period”). Content Length: Generate approximately 300-500 words per section, ensuring enough detail to create a full page of content while maintaining clarity and focus. Be Engaging and Informative: Ensure the content is not only informative but also engaging. Use storytelling elements or highlight the significance of trends to make the analysis compelling."

    detail_adder_prompt = f'You are a professional report writer tasked with generating detailed and engaging content for a multi-page report. The report is about the online presence and activities of a specific target over the last 7 days. You will be provided with a heading, subheadings, and a brief summary. Your job is to expand this information into a comprehensive, well-structured, and detailed section. Details: - Heading: [Insert the heading] - Subheadings: [Insert subheadings, e.g., "Subheading 1", "Subheading 2"] - Summary: [Insert the brief summary] Instructions: 1. Write a detailed introduction for the section based on the heading and summary. 2. Expand each subheading into a detailed subsection: - Include numerical data, insights, and analysis where applicable. - Provide comparisons, psychometric insights, and examples. - Explain the significance of the subtopic and its impact. 3. Conclude the section with a summary of key takeaways and implications. Special Instructions: - Ensure the tone is professional and engaging. - Use data-driven insights and concrete examples to support your writing. - Write content that flows naturally and connects ideas between subsections.'
    # pattern = r"^.*?```json| ```\s.*$"
    # json_response = re.sub( pattern, "", response)
    # html_content = markdown.markdown(content)
    return response

def chat_assist(instructions, prompt):
    chat_response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role": "system", "content": instructions },
            {"role": "user", "content": prompt }
        ]
    )
    return chat_response.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)