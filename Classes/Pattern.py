from ValidationErr import ValidationErr
from pydantic import BaseModel, Field, field_validator, model_validator

class Pattern(BaseModel):

    pattern: str 
    complementary: str
    metPos: int = Field(ge=0)       # Force Integer and >= 0
    metCompPos: int = Field(ge=0)   # Force Integer and >= 0
    valid: bool                     # Valid is a property to filter patterns that are empty

    # Change Valid property.
    # Valid if:
    #   - Pattern and complementary
    #   - Positions not empty
    @model_validator(mode="before")
    @classmethod
    def valid_pattern(self, data: any):
        if isinstance(data, dict):          # Ensure the entry data is a dictionary of properties and values
            if data["pattern"] is "" or data["complementary"] is "":
                data["valid"] = False
        return self

    # Validation to ensure patterns are in IUPAC
    @field_validator("pattern", "complementary")
    @classmethod
    def IUPAC_validation(self, pat: str):
        for char in pat:
            if not char in "ACGTURYSWKMBDHVN":
                raise ValidationErr("Pattern incorrect, no correct IUPAC values.")
        return pat

    def __str__(self):
        return f"{self.pattern}: {self.complementary} | {self.metPos}: {self.metCompPos}"