app.config(function ($routeProvider) {
    $routeProvider.when('/subscribe/', {
        templateUrl: '/static/html/subscription.subscribe.html',
        controller: SubscribeCtrl,
        resolve: SubscribeCtrl.resolve
    });
});

app.config(function ($routeProvider) {
    $routeProvider.when('/unsubscribe/', {
        templateUrl: '/static/html/subscription.unsubscribe.html',
        controller: UnsubscribeCtrl,
        resolve: UnsubscribeCtrl.resolve
    });
});
