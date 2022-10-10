import zroya

status = zroya.init(
    app_name="NotifyBot",
    company_name="MyBotCorp",
    product_name="NoBo",
    sub_product="core",
    version="v01"
)

if not status:
    print("Initialization failed")


# zroya is imported and initialized
template = zroya.Template(zroya.TemplateType.ImageAndText4)
#Adds text:
template.setFirstLine("Example notification")
#Adds the button
template.addAction("Ok")

zroya.show(template)