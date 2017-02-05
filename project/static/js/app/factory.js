app.factory('ui', function ($resource, $rootScope, $window, ngProgressLite) {
    return {
        alert: function (msg, type) {
            if (!msg) {
                msg = 'Неизвестная ошибка.';
                type = 'error';
            }

            $window.$.toaster({priority: type || 'info', message: msg});
        },

        progress: ngProgressLite
    };
});

app.factory('api', function ($resource, ui) {
    return function (name, list, error_alert) {
        list = list == undefined ? true : list;
        error_alert = error_alert == undefined ? true : error_alert;

        function apiRow(params) {
            var promise = $resource(params.url, {}, {
                query: {method: params.method, isArray: list}
            }).query(params.query).$promise;

            if (error_alert) {
                promise.catch(function (response) {
                    ui.alert(response.data.detail, 'error');
                });
            }

            return promise;
        }

        return {
            get: function (name, id, params) {
                return apiRow({
                    url: '/api/' +name + '/' + id + '\\/',
                    method: 'GET',
                    query: { id: id }
                });
            },
            getObject: function (id) {
                list = false;

                return apiRow({
                    url: '/api/' +name + '/' + id + '\\/',
                    method: 'GET'
                });
            },

            getPage: function (page, count) {
                list = false;

                return apiRow({
                    url: '/api/' +name + '\\/',
                    method: 'GET',
                    query: {
                        page: page || 1,
                        count: count || 10
                    }
                });
            }
        };
    }
})
;

app.factory('BBCode', function () {
    XBBCODE.addTags({
        'google': {
            openTag: function (params, content) {
                var website = 'http://www.google.com/#q=' + content;
                return '<a href="' + website + '" target="_blank">';
            },
            closeTag: function (params, content) {
                return '</a>';
            }
        },
        'youtube': {
            openTag: function (params, content) {
                var src = 'https://www.youtube.com/embed/' + content;
                return '<div class="xbbcode-yt">' +
                    '<iframe src="' + src + '" frameborder="0" allowfullscreen>';
            },
            closeTag: function (params, content) {
                return '</iframe></div>';
            }
        },
        'not-copy': {
            openTag: function (params, content) {
                return '<span oncopy="alert(\'gettext(Copying is prohibited.)\');return false">';
            },
            closeTag: function (params, content) {
                return '</span>';
            }
        }
    });

    return {
        render: function (text) {
            return XBBCODE.process({
                text: text || '',
                removeMisalignedTags: true,
                addInLineBreaks: true
            }).html;
        }
    };
});