def user_listing_path(instance,filename):
    return 'user_{0}/listing/{1}'.format(instance.user.id,filename)