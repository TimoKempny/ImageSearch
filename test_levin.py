from itertools import count
from ImageCrawling import build_small, database_tools
from ImageCrawling import feature_interface
from ImageCrawling import hashing_interface
from ImageCrawling import toolbox
from ImageCrawling import crawl_shutterstock
from ImageCrawling import extractors
import ImageCrawling
import numpy as np
import io

if __name__ == '__main__':
    # ImageCrawling.calculate_features("test.db", "mobile_net", feature_interface.mobileNet_func, hashing_interface.dummy_hashing_func, count=0)
    # image = toolbox.get_test_image()[2]
    # toolbox.binary_to_image(image).show()
    # images = ImageCrawling.get_nearest_images("test.db", image, "cifar10-like", "mobile_net", feature_interface.mobileNet_func, count=10)

    # for i in images:
    #     i[0].show()
    # print(crawl_shutterstock.get_image_urls("horse", 200, True))
    # crawl_shutterstock.get_image_count("horse", headless=False)
    # print(crawl_shutterstock.get_image_count("horse", headless=True))
    # links = crawl_shutterstock.crawl_page("horse", 1, headless=True)
    # links = crawl_shutterstock.crawl_links("horse", 500, 5)
    # print(len(links))

    # conn = database_tools.connect("test.db")
    # database_tools.drop_db_from_images(conn, "cifar10-like")
    # database_tools.print_info_images(conn)
    # conn.close()

    # ImageCrawling.crawl_images("horse", "cifar10-like", 10, 0, 1)
    # ImageCrawling.print_db_info("light_database.db")

    # database_tools.create_db("test.db")

    # ImageCrawling.crawl_from_txt("ImageDatabases/keywords.txt", "test.db", "big", 20, 2, main_threads=10, child_threads=1)

    # ImageCrawling.calculate_features("test.db", "mobile_net", feature_interface.mobileNet_func, hashing_interface.dummy_hashing_func, count=0)
    # ImageCrawling.print_db_info("test.db")

    # database_tools.create_db("test2.db")
    # ImageCrawling.crawl_from_txt("ImageDatabases/keywords2.txt", "test2.db", "big", 20, 2, main_threads=1, child_threads=1)

    # conn = database_tools.connect("test.db")
    # # database_tools.create_feature_table(conn)
    # database_tools.calculate_features(conn, "mobile_net", feature_interface.mobileNet_func, hashing_interface.calculate_hashes, count=0)
    # database_tools.print_table(conn, "features", 20, 100)
    # conn.close()

    # image = toolbox.binary_to_image(toolbox.get_test_image()[2])
    # image.show()
    # mobilenet_extractor = extractors.MobileNet()
    # feature = mobilenet_extractor.extractImage(image)


    # images = ImageCrawling.get_nearest_images_2("test.db", image, "big", "mobile_net", feature, count=10)

    # toolbox.base64_to_image(images[0][0]).show()

    # ImageCrawling.create_db("final.db")
    # ImageCrawling.print_db_info("final.db")

    # ImageCrawling.crawl_from_txt("ImageDatabases/keywords2.txt", "final.db", "big", 20, 2, main_threads=1, child_threads=1)

    # ---------------- Am Server ausführen
    # TODO: schon gecrawlte Keywords nicht mehr crawlen
    # database_tools.save_db_info("final.db", "database_log.txt")
    # ImageCrawling.crawl_from_txt("ImageDatabases/keywords.txt", "final.db", "big", 2200, 200, main_threads=5, child_threads=10)
    # database_tools.save_db_info("final.db", "database_log_after.txt")
    # ImageCrawling.calculate_all_features("final.db", count=0)
    # ImageCrawling.print_db_info("final.db")
    # ImageCrawling.calculate_metric("final.db", "big")


    ## -------------- Testing andere Netze
    image = toolbox.binary_to_image(toolbox.get_test_image()[2])
    # image.show()
    mobilenet_extractor = extractors.MobileNet()
    feature = mobilenet_extractor.extractImage(image)
    # ImageCrawling.print_db_info("test.db")
    # print(ImageCrawling.get_images("final.db", "airplane"))


    images, path = ImageCrawling.get_nearest_images_2("final.db", image, "big", "mobile_net", feature, count=10)
    print(path)
    # buf = io.BytesIO()
    # np.save(buf, feature)
    # binary_feature =  buf.getvalue()
    # print(ImageCrawling.search_for_classes("test.db", "big", ImageCrawling.mobileNet, binary_feature, count=15))
    # print(ImageCrawling.calculate_class_score("test.db", "big", ImageCrawling.mobileNet, "tank"))
    # print(ImageCrawling.calculate_network_score("test.db", "big", ImageCrawling.mobileNet))
    # ImageCrawling.calculate_metric("test.db", "big")

    # for i in images:
    #     toolbox.base64_to_image(i[0]).show()

    # ImageCrawling.calculate_all_features("test.db", count=0)

    # database_tools.print_db_info("test.db")
    # database_tools.save_db_info("test.db", "database_log.txt")
