def get_image(url, driver, save_to):
    driver.get(url)

    img_objs = driver.find_elements(By.CLASS_NAME, 'image-grid-image')
    img_style = [image.get_attribute('style') for image in img_objs]
    img_urls = [link.split('url("')[1][:-3] for link in img_style]
    sleeps = [1,0.5,1.5,0.7]

    save_to = save_to
    if save_to is None:
        save_to = 'gotImage'

    save_path = os.path.join('Images', save_to)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for i,link in enumerate(tqdm(img_urls)):
        img_name = i.split['/'][-3]
        save_img = os.path.join(save_path, f'{img_name}.jpeg')
        urllib.request.urlretrieve(link, save_img)
        time.sleep(np.random.choice(sleeps))

