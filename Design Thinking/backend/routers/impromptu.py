from fastapi import APIRouter, HTTPException
import random

router = APIRouter()

TOPICS_DATABASE = [
    {
        "topic": "The Impact of Generative AI on the Future of Creative Work",
        "key_terms": ["Augmented Creativity", "Intellectual Property", "Human-in-the-Loop"],
        "trend_data": "78% of designers leverage AI tools for rapid ideation",
        "outline": "1. Opening: AI as collaborator, not competitor. 2. Core: Shift toward creative direction. 3. Call to Action: Upskilling in AI workflows."
    },
    {
        "topic": "Should Asynchronous Remote Work Replace Fixed Office Hours?",
        "key_terms": ["Deep Work", "Output-Based Culture", "Global Talent Pool"],
        "trend_data": "42% higher retention in flexible work organizations",
        "outline": "1. Hook: The illusion of the 9-to-5. 2. Benefits of autonomy. 3. Overcoming isolation & team alignment."
    },
    {
        "topic": "Accelerating Clean Energy: Innovations Beyond Solar and Wind",
        "key_terms": ["Next-Gen Geothermal", "Solid-State Batteries", "Grid Modernization"],
        "trend_data": "Clean tech investment grew by $1.8T globally in recent years",
        "outline": "1. The scale of the energy transition. 2. Emerging breakthroughs in energy storage. 3. Economic imperative."
    },
    {
        "topic": "The Psychology of First Impressions in Executive Leadership",
        "key_terms": ["Micro-Expressions", "Vocal Presence", "Active Listening"],
        "trend_data": "First impressions form in under 7 seconds of speaking",
        "outline": "1. Hook: The subtle cues that build trust. 2. Non-verbal congruence with message. 3. Practical executive presence habits."
    },
    {
        "topic": "Ethical Governance in Autonomous Decision-Making Systems",
        "key_terms": ["Algorithmic Transparency", "Accountability Frameworks", "Bias Mitigation"],
        "trend_data": "65+ countries drafted AI safety standards in 2024-2025",
        "outline": "1. High-stakes AI decisions in healthcare & finance. 2. The black box dilemma. 3. Designing human oversight."
    },
    {
        "topic": "Commercial Space Exploration: Economic Frontier or Vanity Project?",
        "key_terms": ["Satellite Constellations", "Reusable Rockets", "Orbital Manufacturing"],
        "trend_data": "The global space economy is projected to reach $1.8T by 2035",
        "outline": "1. Evolution from government space race to commercial venture. 2. Earth-bound benefits. 3. Long-term planetary stewardship."
    }
]

@router.get("/impromptu-topic")
async def get_random_topic():
    """Return a randomly selected impromptu topic with research assistant pills and outline."""
    item = random.choice(TOPICS_DATABASE)
    return {
        "topic": item["topic"],
        "key_terms": item["key_terms"],
        "trend_data": item["trend_data"],
        "outline": item["outline"]
    }
