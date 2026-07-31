from typing import TypedDict, Annotated, Optional, Literal
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from model_tinyllama.model import model


class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[
        Literal["pos", "neg", "neu"],
        "Return sentiment as pos, neg or neu"
    ]
    pros: Annotated[Optional[list[str]], "Write all pros in a list"]
    cons: Annotated[Optional[list[str]], "Write all cons in a list"]
    name: Annotated[Optional[str], "Name of the reviewer"]


print("Model Type:", type(model))

structured_model = model.with_structured_output(Review)

review = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware. The $1,300 price tag is also a hard pill to swallow.

Pros:
- Powerful processor
- Excellent camera
- Long battery life
- S-Pen support

Review by Nitish Singh
"""

try:
    result = structured_model.invoke(review)

    print("\nResult:")
    print(result)

    if result is None:
        print("\nStructured output returned None.")
    else:
        print("\nReviewer:", result["name"])

except Exception as e:
    print("\nError:", e)