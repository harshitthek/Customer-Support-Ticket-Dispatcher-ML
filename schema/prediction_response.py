from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    predicted_team: str = Field(
        ...,
        description="The predicted Team to handle the support ticket",
        example="Billing"
    )
    confidence: float = Field(
        ...,
        description="Model's confidence score for the predicted Team (range: 0 to 1)",
        example=0.8432
    )
    urgency_score: float = Field(
        ...,
        description="Urgency Score for the ticket",
        example=0.9354
    )