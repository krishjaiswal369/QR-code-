import qrcode

# Array containing your 10 Google Drive resume links
resume_links = [
    "https://drive.google.com/file/d/1KrWdOeFoWdfdR9xVQLwPVMKFWGRSfMU4/view?usp=drivesdk",
    "https://drive.google.com/file/d/1yyv08xTigAAlCdt-0t3WdsuVR1uxKYJY/view?usp=drivesdk",
    "https://drive.google.com/file/d/1bz6k4znijIiYo5TJq4xPlfkGLqCpROOl/view?usp=drivesdk",
    "https://drive.google.com/file/d/1OBCOdP4K3kXqMeXzI90CyebGC7Ll27yx/view?usp=drivesdk",
    "https://drive.google.com/file/d/1NXlKtXW12pwzf-gvPLUDxuqmCsRysxmv/view?usp=drivesdk",
    "https://drive.google.com/file/d/1cf2i8BRs4L-Y3HYOEoM4iWPVzAOUH7XP/view?usp=drivesdk",
    "https://drive.google.com/file/d/1edU-6vTF-FG5qlQQd4S4X6BXEuvnCj9V/view?usp=drivesdk",
    "https://drive.google.com/file/d/1R_tkbaZm3mjUfNP37b4Jc5yqXf1s_EwZ/view?usp=drivesdk",
    "https://drive.google.com/file/d/1QV3zgLVtLyJil7TRsHV--HtCSaYyMCTi/view?usp=drivesdk",
    "https://drive.google.com/file/d/14-4znC03FV6_rF9wUViPCoDMzrcsYBjD/view?usp=drivesdk"
]

# Loop through each link, generate the QR code, and save as resume_qr_1.png, resume_qr_2.png, etc.
for index, link in enumerate(resume_links, start=1):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"resume_qr_{index}.png"
    img.save(filename)
    print(f"Generated: {filename}")

print("All 10 resume QR codes generated successfully!")
