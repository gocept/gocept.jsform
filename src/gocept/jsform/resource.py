import fanstatic
import js.classy
import js.jquery
import js.knockout

try:
    import js.bootstrap
    import js.jqueryui
except ImportError:
    HAS_CONTAINER_DEPENDENCIES = False
else:
    HAS_CONTAINER_DEPENDENCIES = True

library = fanstatic.Library('gocept.jsform', 'resources')
additionals = fanstatic.Library('gocept.jsform.additional', 'additional')

handlebars = fanstatic.Resource(additionals, 'handlebars-v4.0.2.js')


ko_mapping = fanstatic.Resource(
    additionals, 'ko.mapping.js', minified='ko.mapping.min.js',
    depends=[js.knockout.knockout])

helpers = fanstatic.Resource(
    library, 'helpers.js', minified='helpers.min.js',
    depends=[js.jquery.jquery, ko_mapping])

template = fanstatic.Resource(
    library, 'template.js', minified='template.min.js',
    depends=[helpers])

templates = fanstatic.Resource(
    library, 'templates.js', minified='templates.min.js')

jsform_js = fanstatic.Resource(
    library, 'jsform.js', minified='jsform.min.js',
    depends=[
        template,
        helpers,
        js.classy.classy,
        handlebars,
        js.jquery.jquery,
        templates,
    ])

localization_de = fanstatic.Resource(
    library, 'localizations/de.js', minified='localizations/de.min.js',
    depends=[jsform_js])

localization_en = fanstatic.Resource(
    library, 'localizations/en.js', minified='localizations/en.min.js',
    depends=[jsform_js])

jsform = fanstatic.Group([
    jsform_js,
    localization_de,
    localization_en,
])

if HAS_CONTAINER_DEPENDENCIES is True:

    container_widget = fanstatic.Resource(
        library, 'collection.js', minified='collection.min.js',
        depends=[
            js.bootstrap.bootstrap_css,
            js.bootstrap.bootstrap_js,
            js.jquery.jquery,
            js.jqueryui.bootstrap,
            jsform,
        ])

    list_widget = container_widget  # backwards compatibility
