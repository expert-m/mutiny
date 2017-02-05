app.factory('apiAuth', function ($resource, ui) {
    return {
        login: function (data) {
            return $resource('/api/auth\\/', {}, {
                query: {method: 'GET'}
            }).query(data).$promise.catch(function (data) {
                ui.alert(data.detail);
            });
        },
        logout: function () {
            return $resource('/api/auth\\/', {}, {
                query: {method: 'DELETE'}
            }).query().$promise.catch(function (data) {
                ui.alert(data.detail);
            });
        },
        register: function (data) {
            return $resource('/api/auth\\/', {}, {
                query: {method: 'PUT'}
            }).query(data).$promise.catch(function (data) {
                ui.alert(data.detail);
            });
        }
    }
});

app.factory('apiProfile', function ($resource) {
    return {
        get: function () {
            return $resource('/api/profile\\/', {}, {
                query: {method: 'GET'}
            }).query().$promise.catch(function (data) {
                ui.alert(data.detail);
            });
        },
        save: function (data) {
            return $resource('/api/profile\\/', {}, {
                query: {method: 'POST'}
            }).query(data).$promise.catch(function (data) {
                ui.alert(data.detail);
            });
        },
        remove: function () {
            return $resource('/api/profile\\/', {}, {
                query: {method: 'DELETE'}
            }).query().$promise.catch(function (data) {
                ui.alert(data.detail);
            });
        }
    }
});
