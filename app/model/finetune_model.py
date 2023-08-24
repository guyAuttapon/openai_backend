from pydantic import BaseModel, Field


class Train_model(BaseModel):
    training_file: str
    validation_file: str | None = Field(
        default=None
    )
    model: str | None = Field(
        default=None
    )
    n_epochs: int | None = Field(
        default=None
    )
    batch_size: int | None = Field(
        default=None
    )
    learning_rate_multiplier: float | None = Field(
        default=None
    )
    prompt_loss_weight: float | None = Field(
        default=None
    )
    compute_classification_metrics: bool | None = Field(
        default=None
    )
    classification_n_classes: int | None = Field(
        default=None
    )
    classification_positive_class: str | None = Field(
        default=None
    )
    suffix: str | None = Field(
        default=None
    )