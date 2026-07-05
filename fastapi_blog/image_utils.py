import uuid
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageOps

profile_pics_dir = Path("media/profile_pics")

def process_profile_image(content: bytes) -> tuple[bytes, str]:
    with Image.open(BytesIO(content)) as original:
        img = ImageOps.exif_transpose(original)

        img = ImageOps.fit(img, (300, 300), method=Image.Resampling.LANCZOS)

        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB")

        filename = f"{uuid.uuid4().hex}.jpg"
        filepath = profile_pics_dir / filename
        profile_pics_dir.mkdir(parents=True, exist_ok=True)

        img.save(filepath, "JPEG", quality=85, optimize=True)
        
        # output = BytesIO()
        # img.save(output, "JPEG", quality=85, optimize=True)
        # output.seek(0)

    return filename

def delete_profile_image(filename: str | None) -> None:
    if not filename:
        return
    
    filepath = profile_pics_dir / filename
    if filepath.exists():
        filepath.unlink()