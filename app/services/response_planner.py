"""
Response Planner

Decides:
- Response length
- Sections
- Code example
- Detailed explanation
"""

from app.config.settings import settings


class ResponsePlanner:

    def plan(self, question: str):

        question_lower = question.lower()

        # ---------- SHORT ----------
        if len(question.split()) <= 5:

            return {
                "max_tokens": settings.SHORT_RESPONSE_TOKENS,
                "style": "short",
                "sections": [
                    "Definition",
                    "Working",
                    "Conclusion"
                ],
                "include_code": False,
                "include_details": False,
            }

        # ---------- LONG ----------
        elif any(word in question_lower for word in [

            "explain",
            "internally",
            "architecture",
            "working",
            "deep",
            "detail",
            "how",
            "why",

        ]):

            return {
                "max_tokens": settings.LONG_RESPONSE_TOKENS,
                "style": "long",
                "sections": [
                    "Definition",
                    "Working",
                    "Java Example",
                    "Detailed Explanation",
                    "Conclusion"
                ],
                "include_code": True,
                "include_details": True,
            }

        # ---------- MEDIUM ----------

        return {

            "max_tokens": settings.MEDIUM_RESPONSE_TOKENS,

            "style": "medium",

            "sections": [
                "Definition",
                "Working",
                "Java Example",
                "Conclusion"
            ],

            "include_code": True,

            "include_details": False,
        }