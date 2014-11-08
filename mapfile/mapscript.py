        # create a new mapfile from scratch
        self.map = mapscript.mapObj()
        self.map.save('temp.map')
        self.map.setSize(256,256)
        self.map.setExtent(-180.0,-90.0,180.0,90.0)
        self.map.units= mapscript.MS_DD
        self.map.imagecolor.setRGB(255,255,255)


def Class( oDjClass ):

    oMSClass = mapscript.classObj()

    #d backgroundcolor     = ColorField( ) */
    #d color               = ColorField( ) */
    #  DEBUG [on|off] */

    oMSClass.expression     = oDjClass.expression
    oMSClass.group          = oDjClass.group
    oMSClass.keyimage       = oDjClass.keyimage

    label               `   = models.ForeignKey('label')
    leader                  = models.ForeignKey('leader')

    oMSClass.maxscaledenom  = oDjClass.maxscaledenom
    #oMSClass.maxsize       = oDjClass.maxsize
    oMSClass.minscaledenom  = oDjClass.minscaledenom
    #oMSClass.minsize       = oDjClass.minsize

    oMSClass.name           = oDjClass.name

    #d outlinecolor        = ColorField( ) */
    #d size                = models.IntegerField()*/

    oMSClass.status          = oDjClass.status

    style               = models.ManyToManyField(style)

    oMSClass.group          = oDjClass.group

    #d symbol              = models.CharField(                  max_length = 2048)

    oMSClass.group          = oDjClass.group
    oMSClass.group          = oDjClass.group


    template            = models.CharField(                  max_length = 2048)
    text                = models.CharField(                  max_length = 2048)


    validation          = models.ManyToManyField(validation)


An instance of classObj is associated with with one instance of layerObj:

+-------+ 0..*     1 +-------+
| Class | <--------> | Layer |
+-------+            +-------+

The other important associations for classObj are with styleObj, labelObj, and hashTableOb

+-------+ 1     0..* +-------+
| Class | ---------> | Style |
+-------+            +-------+

+-------+ 1     0..* +-------+
| Class | ---------> | Label |
+-------+            +-------+

+-------+ 1        1 +-----------+
| Class | ---------> | HashTable |
+-------+            |    --     |
                     | metadata  |
                     +-----------+

Multiple class styles have been supported since 4.1, and multiple class labels since 6.2. See the styleObj section for details on use of multiple class styles.
classObj Attributes

debug : int
    MS_TRUE or MS_FALSE
keyimage : string
    TODO Not sure what this attribute is for
label : labelObj immutable
    Definition of class labeling. Removed (6.2) - use addLabel, getLabel and removeLabel instead.
layer : layerObj immutable
    Reference to the parent layer
maxscaledenom : float
    The minimum scale at which class is drawn
metadata : hashTableObj immutable
    class metadata hash table.
minscaledenom : float
    The maximum scale at which class is drawn
name : string
    Unique within a layer
numlabels : int

    Number of labels for class.

    New in version 6.2.
numstyles : int
    Number of styles for class. In the future, probably the 4.4 release, this attribute will be made immutable.
status : int
    MS_ON or MS_OFF. Draw features of this class or do not.
template : string
    Template for queries
title : string
    Text used for legend labeling
type : int
    The layer type of its parent layer

classObj Methods

new classObj( [ layerObj parent_layer=NULL ] ) : classObj
    Create a new child classObj instance at the tail (highest index) of the class array of the parent_layer. A class can be created outside the context of a parent layer by omitting the single constructor argument.
addLabel( labelObj ) : int

    Add a labelObj to the classObj and return its index in the labels array.

    New in version 6.2.
clone( ) : classObj
    Return an independent copy of the class without a parent layer.
createLegendIcon( mapObj map, layerObj layer, int width, int height ) : imageObj
    Draw and return a new legend icon.
drawLegendIcon( mapObj map, layerObj layer, int width, int height, imageObj image, int dstx, int dsty ) : int
    Draw the legend icon onto image at dstx, dsty. Returns MS_SUCCESS or MS_FAILURE.
getExpressionString() : string
    Return a string representation of the expression enclosed in the quote characters appropriate to the expression type.
getFirstMetaDataKey() : string

    Returns the first key in the metadata hash table. With getNextMetaDataKey(), provides an opaque iterator over keys.

    Note

    getFirstMetaDataKey(), getMetaData(), and getNextMetaDataKey() are deprecated and will be removed in a future version. Replaced by direct metadata access, see hashTableObj.
getLabel( int index ) : labelObj

    Return a reference to the labelObj at index in the labels array.

    See the labelObj section for more details on multiple class labels.

    New in version 6.2.
getMetaData( string key ) : string

    Return the value of the classObj metadata at key.

    Note

    getFirstMetaDataKey(), getMetaData(), and getNextMetaDataKey() are deprecated and will be removed in a future version. Replaced by direct metadata access, see hashTableObj.
getNextMetaDataKey( string lastkey ) : string

    Returns the next key in the metadata hash table or NULL if lastkey is the last valid key. If lastkey is NULL, returns the first key of the metadata hash table.

    Note

    getFirstMetaDataKey(), getMetaData(), and getNextMetaDataKey() are deprecated and will be removed in a future version. Replaced by direct metadata access, see hashTableObj.
getStyle( int index ) : styleObj

    Return a reference to the styleObj at index in the styles array.

    See the styleObj section for more details on multiple class styles.
getTextString() : string
    Return a string representation of the text enclosed in the quote characters appropriate to the text expression type (logical or simple string).
insertStyle( styleObj style [, int index=-1 ] ) : int
    Insert a copy of style into the styles array at index index. Default is -1, or the end of the array. Returns the index at which the style was inserted.
moveStyleDown( int index ) : int
    Swap the styleObj at index with the styleObj index + 1.
moveStyleUp( int index ) : int
    Swap the styleObj at index with the styleObj index - 1.
removeLabel( int index ) : labelObj

    Remove the labelObj at index from the labels array and return a reference to the labelObj. numlabels is decremented, and the array is updated.

    New in version 6.2.
removeStyle( int index ) : styleObj
    Remove the styleObj at index from the styles array and return a copy.
setExpression( string expression ) : int
    Set expression string where expression is a MapServer regular, logical or string expression. Returns MS_SUCCESS or MS_FAILUIRE.
setMetaData( string key, string value ) : int

    Insert value into the classObj metadata at key. Returns MS_SUCCESS or MS_FAILURE.

    Note

    setMetaData() is deprecated and will be removed in a future version. Replaced by direct metadata access, see hashTableObj.
setText( string text ) : int

    Set text string where text is a MapServer text expression. Returns MS_SUCCESS or MS_FAILUIRE.

    Note

    Older versions of MapScript (pre-4.8) featured the an undocumented setText() method that required a layerObj be passed as the first argument. That argument was completely bogus and has been removed.

colorObj

Since the 4.0 release, MapServer colors are instances of colorObj. A colorObj may be a lone object or an attribute of other objects and have no other associations.
colorObj Attributes

blue : int
    Blue component of color in range [0-255]
green : int
    Green component of color in range [0-255]
pen : int

    Don’t mess with this unless you know what you are doing!

    Note

    Because of the issue with pen, setting colors by individual components is unreliable. Best practice is to use setRGB(), setHex(), or assign to a new instance of colorObj().
red : int
    Red component of color in range [0-255]

colorObj Methods

new colorObj( [ int red=0, int green=0, int blue=0, int pens=-4 ] ) : colorObj
    Create a new instance. The color arguments are optional.
setHex( string hexcolor ) : int
    Set the color to values specified in case-independent hexadecimal notation. Calling setHex(‘#ffffff’) assigns values of 255 to each color component. Returns MS_SUCCESS or MS_FAILURE.
setRGB( int red, int green, int blue ) : int
    Set all three RGB components. Returns MS_SUCCESS or MS_FAILURE.
toHex() : string
    Complement to setHex, returning a hexadecimal representation of the color components.

errorObj

This class allows inspection of the MapServer error stack. Only needed for the Perl module as the other language modules expose the error stack through exceptions.
errorObj Attributes

code : int
    MapServer error code such as MS_IMGERR (1).
message : string
    Context-dependent error message.
routine : string
    MapServer function in which the error was set.

errorObj Methods

next : errorObj
    Returns the next error in the stack or NULL if the end has been reached.

fontSetObj

A fontSetObj is always a ‘fontset’ attribute of a mapObj.
fontSetObj Attributes

filename : string immutable
    Path to the fontset file on disk.
fonts : hashTableObj immutable
    Mapping of fonts.
numfonts : int immutable
    Number of fonts in set.

fontSetObj Methods

None
hashTableObj

A hashTableObj is a very simple mapping of case-insensitive string keys to single string values. Map, Layer, and Class metadata have always been hash hables and now these are exposed directly. This is a limited hash that can contain no more than 41 values.
hashTableObj Attributes

numitems : int immutable
    Number of hash items.

hashTableObj Methods

clear( ) : void
    Empties the table of all items.
get( string key [, string default=NULL ] ) : string
    Returns the value of the item by its key, or default if the key does not exist.
nextKey( [string key=NULL] ) : string
    Returns the name of the next key or NULL if there is no valid next key. If the input key is NULL, returns the first key.
remove( string key ) : int
    Removes the hash item by its key. Returns MS_SUCCESS or MS_FAILURE.
set( string key, string value ) : int
    Sets a hash item. Returns MS_SUCCESS or MS_FAILURE.

imageObj

An image object is a wrapper for GD and GDAL images.
imageObj Attributes

format : outputFormatObj immutable
    Image format.
height : int immutable
    Image height in pixels.
imagepath : string immutable
    If image is drawn by mapObj.draw(), this is the mapObj’s web.imagepath.
imageurl : string immutable
    If image is drawn by mapObj.draw(), this is the mapObj’s web.imageurl.
renderer : int
    MS_RENDER_WITH_GD, MS_RENDER_WITH_SWF, MS_RENDER_WITH_RAWDATA, MS_RENDER_WITH_PDF, or MS_RENDER_WITH_IMAGEMAP. Don’t mess with this!
size : int immutable

    To access this attribute use the getSize method.

    Note

    the getSize method is inefficient as it does a call to getBytes and then computes the size of the byte array. The bytearray is then immediately discarded. In most cases it is more efficient to call getBytes directly.
width : int immutable
    Image width in pixels.

imageObj Methods

new imageObj( int width, int height [, outputFormatObj format=NULL [, string filename=NULL ] ] ) : imageObj
    Create new instance of imageObj. If filename is specified, an imageObj is created from the file and any specified width, height, and format parameters will be overridden by values of the image in filename. Otherwise, if format is specified an imageObj is created using that format. See the format attribute above for details. If filename is not specified, then width and height should be specified.
getBytes() : binary data
    Returns the image contents as a binary buffer. The exact form of this buffer will vary by mapscript language (eg. string in Python, byte[] array in Java and C#, unhandled in perl)
getSize() : int

    Resturns the size of the binary buffer representing the image buffer.

    Note

    the getSize method is inefficient as it does a call to getBytes and then computes the size of the byte array. The byte array is then immediately discarded. In most cases it is more efficient to call getBytes directly.
save( string filename [, mapObj parent_map=NULL ] ) : int
    Save image to filename. The optional parent_map parameter must be specified if saving GeoTIFF images.
write( [ FILE file=NULL ] ) : int

    Write image data to an open file descriptor or, by default, to stdout. Returns MS_SUCCESS or MS_FAILURE.

    Note

    This method is current enabled for Python and C# only. C# supports writing onto a Stream object. User-contributed typemaps are needed for Perl, Ruby, and Java.

Note

The free() method of imageObj has been deprecated. In MapServer revisions 4+ all instances of imageObj will be properly disposed of by the interpreter’s garabage collector. If the application can’t wait for garabage collection, then the instance can simply be deleted or undef’d.
intarray

An intarray is a utility class generated by SWIG useful for manipulating map layer drawing order. See mapObj::getLayersDrawingOrder for discussion of mapscript use and see http://www.swig.org/Doc1.3/Library.html#Library_nn5 for a complete reference.
intarray Attributes

None
intarray Methods

new intarray( int numitems ) : intarray
    Returns a new instance of the specified length.

labelCacheMemberObj

An individual feature label. The labelCacheMemberObj class is associated with labelCacheObj:

+------------------+ 0..*     1 +------------+
| LabelCacheMember | <--------- | LabelCache |
+------------------+            +------------+

labelCacheMemberObj Attributes

classindex : int immutable
    Index of the class of the labeled feature.
featuresize : float immutable
    TODO
label : labelObj immutable
    Copied from the class of the labeled feature.
layerindex : int immutable
    The index of the layer of the labeled feature.
numstyles : int immutable
    Number of styles as for the class of the labeled feature.
point : pointObj immutable
    Label point.
poly : shapeObj immutable
    Label bounding box.
shapeindex : int immutable
    Index within shapefile of the labeled feature.
status : int immutable
    Has the label been drawn or not?
styles : styleObj immutable
    TODO this should be protected from SWIG.
text : string immutable
    Label text.
tileindex : int immutable
    Tileindex of the layer of the labeled feature.

labelCacheMemberObj Methods

None.

Note

No real scripting control over labeling currently, but there may be some interesting new possibilities if users have control over labeling text, position, and status.
labelCacheObj

Set of a map’s cached labels. Has no other existence other than as a ‘labelcache’ attribute of a mapObj. Associated with labelCacheMemberObj and markerCacheMemberObj:

+------------+ 1     0..* +-------------------+
| LabelCache | ---------> | LabelCacheMember  |
+------------+            + ----------------- +
                          | MarkerCacheMember |
                          +-------------------+

labelCacheObj Attributes

cachesize : int immutable
    TODO
markercachesize : int immutable
    TODO
numlabels : int immutable
    Number of label members.
nummarkers : int immutable
    Number of marker members.

labelCacheObj Methods

freeCache( ) : void
    Free the labelcache.

labelObj

A labelObj is associated with a classObj, a scalebarObj, or a legendObj:

+-------+ 0..1     1 +----------+
| Label | <--------- | Scalebar |
+-------+            | -------- |
                     | Legend   |
                     +----------+

+-------+ 0..*     1 +-------+
| Label | <--------- | Class |
+-------+            +-------+

An instance of labelObj can exist outside of a classObj container and be explicitly inserted into the classObj:

new_label = new labelObj()
the_class.addLabel(new_label)

labelObj Attributes

angle : float
    TODO
antialias : int
    MS_TRUE or MS_FALSE
autoangle : int
    MS_TRUE or MS_FALSE
autofollow : int
    MS_TRUE or MS_FALSE. Tells mapserver to compute a curved label for appropriate linear features (see MS RFC 11: Support for Curved Labels for specifics).
autominfeaturesize: int
    MS_TRUE or MS_FALSE
backgroundcolor : colorObj

    Color of background rectangle or billboard.

    Deprecated since version 6.0: Use styleObj and geomtransform.
backgroundshadowcolor : colorObj

    Color of background rectangle or billboard shadow.

    Deprecated since version 6.0: Use styleObj and geomtransform.
backgroundshadowsizex : int

    Horizontal offset of drop shadow in pixels.

    Deprecated since version 6.0: Use styleObj and geomtransform.
backgroundshadowsizey : int

    Vertical offset of drop shadow in pixels.

    Deprecated since version 6.0: Use styleObj and geomtransform.
buffer : int
    Maybe this should’ve been named ‘padding’ since that’s what it is: padding in pixels around a label.
color : colorObj
    Foreground color.
encoding : string
    Supported encoding format to be used for labels. If the format is not supported, the label will not be drawn. Requires the iconv library (present on most systems). The library is always detected if present on the system, but if not the label will not be drawn. Required for displaying international characters in MapServer. More information can be found at: http://www.foss4g.org/FOSS4G/MAPSERVER/mpsnf-i18n-en.html.
font : string
    Name of TrueType font.
force : int
    MS_TRUE or MS_FALSE.
maxsize : int
    Maximum height in pixels for scaled labels. See symbolscale attribute of layerObj.
mindistance : int
    Minimum distance in pixels between duplicate labels.
minfeaturesize : int
    Features of this size of greater will be labeled.
minsize : int
    Minimum height in pixels.
numstyles : int
    Number of label styles
offsetx : int
    Horizontal offset of label.
offsety : int
    Vertical offset of label.
outlinecolor : colorObj
    Color of one point outline.
partials : int
    MS_TRUE (default) or MS_FALSE. Whether or not labels can flow past the map edges.
position : int
    MS_UL, MS_UC, MS_UR, MS_CL, MS_CC, MS_CR, MS_LL, MS_LC, MS_LR, or MS_AUTO.
shadowcolor : colorObj
    Color of drop shadow.
shadowsizex : int
    Horizontal offset of drop shadow in pixels.
shadowsizey : int
    Vertical offset of drop shadow in pixels.
size : int
    Annotation height in pixels.
type : int
    MS_BITMAP or MS_TRUETYPE.
wrap : string
    Character on which legend text will be broken to make multi-line legends.

labelObj Methods

getBinding( int binding ) : string
    Get the attribute binding for a specified label property. Returns NULL if there is no binding for this property.
getExpressionString( ) : string
    Returns the label expression string.
getStyle( int index ) : styleObj
    Return a reference to the styleObj at index in the styles array.
getTextString( ) : string
    Returns the label text string.
insertStyle( styleObj style [, int index=-1 ] ) : int
    Insert a copy of style into the styles array at index index. Default is -1, or the end of the array. Returns the index at which the style was inserted.
moveStyleDown( int index ) : int
    Swap the styleObj at index with the styleObj index + 1.
moveStyleUp( int index ) : int
    Swap the styleObj at index with the styleObj index - 1.
removeBinding( int binding ) : int
    Remove the attribute binding for a specfiled label property.
removeStyle( int index ) : styleObj
    Remove the styleObj at index from the styles array and return a copy.
setBinding ( int binding, string item ) : int

    Set the attribute binding for a specified label property. Binding constants look like this: MS_LABEL_BINDING_[attribute name]:

    setBinding(MS_LABEL_BINDING_COLOR, "FIELD_NAME_COLOR");

setExpression( string expression ) : int
    Set the label expression.
setText( string text ) : int
    Set the label text.
updateFromString ( string snippet ) : int
    Update a label from a string snippet. Returns MS_SUCCESS/MS_FAILURE.

layerObj

A layerObj is associated with mapObj. In the most recent revision, an intance of layerObj can exist outside of a mapObj:

+-------+ 0..*  0..1 +-----+
| Layer | <--------> | Map |
+-------+            +-----+

The other important association for layerObj is with classObj:

+-------+ 1     0..* +-------+
| Layer | <--------> | Class |
+-------+            +-------+

and hashTableObj:

+-------+ 1        1 +-----------+
| Layer | ---------> | HashTable |
+-------+            |    --     |
                     | metadata  |
                     +-----------+

layerObj Attributes

bandsitem : string
    The attribute from the index file used to select the source raster band(s) to be used. Normally NULL for default bands processing.
classitem : string
    The attribute used to classify layer data.
connection : string
    Layer connection or DSN.
connectiontype : int
    See MS_CONNECTION_TYPE in mapserver.h for possible values. When setting the connection type setConnectionType() should be used in order to initialize the layer vtable properly.
data : string
    Layer data definition, values depend upon connectiontype.
debug : int
    Enable debugging of layer. MS_ON or MS_OFF (default).
dump : int

    Since 6.0, dump is not available anymore. metadata is used instead.

    Switch to allow mapserver to return data in GML format. MS_TRUE or MS_FALSE. Default is MS_FALSE.

    Deprecated since version 6.0: metadata is used instead.
extent : rectObj
    optional limiting extent for layer features.
filteritem : string
    Attribute defining filter.
footer : string
    TODO
group : string
    Name of a group of layers.
header : string
    TODO
index : int immutable
    Index of layer within parent map’s layers array.
labelangleitem : string
    Attribute defining label angle.
labelcache : int
    MS_ON or MS_OFF. Default is MS_ON.
labelitem : string
    Attribute defining feature label text.
labelmaxscaledenom : float
    Minimum scale at which layer will be labeled.
labelminscaledenom : float
    Maximum scale at which layer will be labeled.
labelrequires : string
    Logical expression.
labelsizeitem : string
    Attribute defining label size.
map : mapObj immutable
    Reference to parent map.
mask : string
    Layer name for masking. (MS RFC 79: Layer Masking)
maxfeatures : int
    Maximum number of layer features that will be drawn. For shapefile data this means the first N features where N = maxfeatures.
maxscaledenom : float
    Minimum scale at which layer will be drawn.
metadata : hashTableObj immutable
    Layer metadata.
minscaledenom : float
    Maximum scale at which layer will be drawn.
name : string
    Unique identifier for layer.
numclasses : int immutable
    Number of layer classes.
numitems : int immutable
    Number of layer feature attributes (items).
numjoins : int immutable
    Number of layer joins.
numprocessing : int immutable
    Number of raster processing directives.
offsite : colorObj
    transparent pixel value for raster layers.
opacity : int
    Layer opacity percentage in range [0, 100]. The special value of MS_GD_ALPHA (1000) indicates that the alpha transparency of pixmap symbols should be honored, and should be used only for layers that use RGBA pixmap symbols.
postlabelcache : int
    MS_TRUE or MS_FALSE. Default is MS_FALSE.
requires : string
    Logical expression.
sizeunits : int
    Units of class size values. MS_INCHES, MS_FEET, MS_MILES, MS_NAUTICALMILES, MS_METERS, MS_KILOMETERS, MS_DD or MS_PIXELS
status : int
    MS_ON, MS_OFF, or MS_DEFAULT.
styleitem : string
    Attribute defining styles.
symbolscaledenom : float
    Scale at which symbols are default size.
template : string
    Template file. Note that for historical reasons, the query attribute must be non-NULL for a layer to be queryable.
tileindex : string
    Layer index file for tiling support.
tileitem : string
    Attribute defining tile paths.
tolerance : float
    Search buffer for point and line queries.
toleranceunits : int
    MS_INCHES, MS_FEET, MS_MILES, MS_NAUTICALMILES, MS_METERS, MS_KILOMETERS, MS_DD or MS_PIXELS
transform : int
    Whether or not layer data is to be transformed to image units. MS_TRUE or MS_FALSE. Default is MS_TRUE. Case of MS_FALSE is for data that are in image coordinates such as annotation points.
type : int
    See MS_LAYER_TYPE in mapserver.h.
units : int
    Units of the layer. See MS_UNITS in mapserver.h.

layerObj Methods

new layerObj( [ mapObj parent_map=NULL ] ) : layerObj
    Create a new layerObj in parent_map. The layer index of the new layerObj will be equal to the parent_map numlayers - 1. The parent_map arg is now optional and Layers can exist outside of a Map.
addFeature( shapeObj shape ) : int
    Add a new inline feature on a layer. Returns -1 on error. TODO: Is this similar to inline features in a mapfile? Does it work for any kind of layer or connection type?
addProcessing( string directive ) : void
    Adds a new processing directive line to a layer, similar to the PROCESSING directive in a map file. Processing directives supported are specific to the layer type and underlying renderer.
applySLD( string sld, string stylelayer ) : int
    Apply the SLD document to the layer object. The matching between the sld document and the layer will be done using the layer’s name. If a namedlayer argument is passed (argument is optional), the NamedLayer in the sld that matchs it will be used to style the layer. See SLD HOWTO for more information on the SLD support.
applySLDURL( string sld, string stylelayer ) : int
    Apply the SLD document pointed by the URL to the layer object. The matching between the sld document and the layer will be done using the layer’s name. If a namedlayer argument is passed (argument is optional), the NamedLayer in the sld that matchs it will be used to style the layer. See SLD HOWTO for more information on the SLD support.
clearProcessing() : int
    Clears the layer’s raster processing directives. Returns the subsequent number of directives, which will equal MS_SUCCESS if the directives have been cleared.
clone() : layerObj
    Return an independent copy of the layer with no parent map.
close() : void
    Close the underlying layer.

Note

demote() is removed in MapServer 4.4

draw( mapObj map, imageObj image ) : int
    Renders this layer into the target image, adding labels to the cache if required. Returns MS_SUCCESS or MS_FAILURE. TODO: Does the map need to be the map on which the layer is defined? I suspect so.
drawQuery( mapObj map, imageObj image ) :
    Draw query map for a single layer into the target image. Returns MS_SUCCESS or MS_FAILURE.
executeWFSGetFeature( layer ) : string
    Executes a GetFeature request on a WFS layer and returns the name of the temporary GML file created. Returns an empty string on error.
generateSLD() : void
    Returns an SLD XML string based on all the classes found in the layer (the layer must have STATUS on).
getClass( int i ) : classObj
    Fetch the requested class object. Returns NULL if the class index is out of the legal range. The numclasses field contains the number of classes available, and the first class is index 0.
getExtent() : rectObj
    Fetches the extents of the data in the layer. This normally requires a full read pass through the features of the layer and does not work for raster layers.
getFeature( int shapeindex [, int tileindex=-1 ] ) : shapeObj

    Return the layer feature at shapeindex and tileindex.

    Note

    getFeature has been removed as of version 6.0 and replaced by getShape
getFilterString() : string
    Returns the current filter expression.
getFirstMetaDataKey() : string

    Returns the first key in the metadata hash table. With getNextMetaDataKey(), provides an opaque iterator over keys.

    Note

    getFirstMetaDataKey(), getMetaData(), and getNextMetaDataKey() are deprecated and will be removed in a future version. Replaced by direct metadata access, see hashTableObj.
getItem( int i ) : string
    Returns the requested item. Items are attribute fields, and this method returns the item name (field name). The numitems field contains the number of items available, and the first item is index zero.
getMetaData( string key ) : string

    Return the value at key from the metadata hash table.

    Note

    getFirstMetaDataKey(), getMetaData(), and getNextMetaDataKey() are deprecated and will be removed in a future version. Replaced by direct metadata access, see hashTableObj.
getNextMetaDataKey( string lastkey ) : string

    Returns the next key in the metadata hash table or NULL if lastkey is the last valid key. If lastkey is NULL, returns the first key of the metadata hash table.

    Note

    getFirstMetaDataKey(), getMetaData(), and getNextMetaDataKey() are deprecated and will be removed in a future version. Replaced by direct metadata access, see hashTableObj.
getNumFeatures() : int
    Returns the number of inline features in a layer. TODO: is this really only online features or will it return the number of non-inline features on a regular layer?
getNumResults() : int
    Returns the number of entries in the query result cache for this layer.
getProcessing( int index) : string
    Return the raster processing directive at index.
getProjection( ) : string
    Returns the PROJ.4 definition of the layer’s projection.
getResult( int i ) : resultCacheMemberObj
    Fetches the requested query result cache entry, or NULL if the index is outside the range of available results. This method would normally only be used after issuing a query operation.
getResults() : resultCacheObj
    Returns a reference to layer’s result cache. Should be NULL prior to any query, or after a failed query or query with no results.
getResultsBounds() : rectObj
    Returns the bounds of the features in the result cache.
getShape( resultCacheMemberObj result ) : int
    Get a shape from layer data. Argument is a result cache member from layerObj::getResult(i)
getWMSFeatureInfoURL( mapObj map, int click_x, int click_y, int feature_count, string info_format ) : string
    Return a WMS GetFeatureInfo URL (works only for WMS layers) clickX, clickY is the location of to query in pixel coordinates with (0,0) at the top left of the image. featureCount is the number of results to return. infoFormat is the format the format in which the result should be requested. Depends on remote server’s capabilities. MapServer WMS servers support only “MIME” (and should support “GML.1” soon). Returns “” and outputs a warning if layer is not a WMS layer or if it is not queriable.
insertClass( classObj class [, int index=-1 ] ) : int
    Insert a copy of the class into the layer at the requested index. Default index of -1 means insertion at the end of the array of classes. Returns the index at which the class was inserted.
isVisible( ) : int
    Returns MS_TRUE or MS_FALSE after considering the layer status, minscaledenom, and maxscaledenom within the context of the parent map.
moveClassDown( int class ) : int
    The class specified by the class index will be moved up into the array of layers. Returns MS_SUCCESS or MS_FAILURE. ex. moveClassDown(1) will have the effect of moving class 1 down to postion 2, and the class at position 2 will be moved to position 1.
moveClassUp( int class ) : int
    The class specified by the class index will be moved up into the array of layers. Returns MS_SUCCESS or MS_FAILURE. ex. moveClassUp(1) will have the effect of moving class 1 up to postion 0, and the class at position 0 will be moved to position 1.
nextShape( ) : shapeObj

    Called after msWhichShapes has been called to actually retrieve shapes within a given area returns a shape object or MS_FALSE

    example of usage:

    mapObj map = new mapObj("d:/msapps/gmap-ms40/htdocs/gmap75.map");
    layerObj layer = map.getLayerByName('road');
    int status = layer.open();
    status = layer.whichShapes(map.extent);
    shapeObj shape;
    while ((shape = layer.nextShape()) != null)
    {
      ...
    }
    layer.close();

open() : void
    Opens the underlying layer. This is required before operations like getFeature() will work, but is not required before a draw or query call.

Note

promote() is eliminated in MapServer 4.4.

queryByAttributes( mapObj map, string qitem, string qstring, int mode ) : int

    Query layer for shapes that intersect current map extents. qitem is the item (attribute) on which the query is performed, and qstring is the expression to match. The query is performed on all the shapes that are part of a CLASS that contains a TEMPLATE value or that match any class in a layer that contains a LAYER TEMPLATE value.

    Note that the layer’s FILTER/FILTERITEM are ignored by this function. Mode is MS_SINGLE or MS_MULTIPLE depending on number of results you want. Returns MS_SUCCESS if shapes were found or MS_FAILURE if nothing was found or if some other error happened.
queryByFeatures( mapObj map, int slayer ) : int
    Perform a query set based on a previous set of results from another layer. At present the results MUST be based on a polygon layer. Returns MS_SUCCESS if shapes were found or MS_FAILURE if nothing was found or if some other error happened
queryByIndex( mapObj map, int shapeindex, int tileindex [, int bAddToQuery=MS_FALSE ]) : int
    Pop a query result member into the layer’s result cache. By default clobbers existing cache. Returns MS_SUCCESS or MS_FAILURE.
queryByPoint( mapObj map, pointObj point, int mode, float buffer ) : int
    Query layer at point location specified in georeferenced map coordinates (i.e. not pixels). The query is performed on all the shapes that are part of a CLASS that contains a TEMPLATE value or that match any class in a layer that contains a LAYER TEMPLATE value. Mode is MS_SINGLE or MS_MULTIPLE depending on number of results you want. Passing buffer <=0 defaults to tolerances set in the map file (in pixels) but you can use a constant buffer (specified in ground units) instead. Returns MS_SUCCESS if shapes were found or MS_FAILURE if nothing was found or if some other error happened.
queryByRect( mapObj map, rectObj rect ) : int
    Query layer using a rectangle specified in georeferenced map coordinates (i.e. not pixels). The query is performed on all the shapes that are part of a CLASS that contains a TEMPLATE value or that match any class in a layer that contains a LAYER TEMPLATE value. Returns MS_SUCCESS if shapes were found or MS_FAILURE if nothing was found or if some other error happened.
queryByShape( mapObj map, shapeObj shape ) : int
    Query layer based on a single shape, the shape has to be a polygon at this point. Returns MS_SUCCESS if shapes were found or MS_FAILURE if nothing was found or if some other error happened
removeClass( int index ) : classObj
    Removes the class indicated and returns a copy, or NULL in the case of a failure. Note that subsequent classes will be renumbered by this operation. The numclasses field contains the number of classes available.
removeMetaData( string key ) : int

    Delete the metadata hash at key. Returns MS_SUCCESS or MS_FAILURE.

    Note

    removeMetaData() is deprecated and will be removed in a future version. Replaced by direct metadata access, see hashTableObj.
resultsGetShape(int shapeindex [, int tileindex = -1]) : shapeObj
    Retrieve shapeObj from a layer’s resultset by index. Tileindex is optional and is used only for tiled shapefiles, Simply omit or pass tileindex = -1 for other data sources. Added in MapServer 5.6.0 due to the one-pass query implementation.
setConnectionType(int connectiontype, string library_str) : int
    Changes the connectiontype of the layer and recreates the vtable according to the new connection type. This method should be used instead of setting the connectiontype parameter directly. In case when the layer.connectiontype = MS_PLUGIN the library_str parameter should also be specified so as to select the library to load by mapserver. For the other connection types this parameter is not used.
setExtent( float minx, float miny, float maxx, float maxy ) : int
    Sets the extent of a layer. Returns MS_SUCCESS or MS_FAILURE.
setFilter( string filter ) : int
    Sets a filter expression similarly to the FILTER expression in a map file. Returns MS_SUCCESS on success or MS_FAILURE if the expression fails to parse.
setMetaData( string key, string value ) : int

    Assign value to the metadata hash at key. Return MS_SUCCESS or MS_FAILURE.

    Note

    setMetaData() is deprecated and will be removed in a future version. Replaced by direct metadata access, see hashTableObj.
setProcessingKey( string key, string value ) : void
    Adds or replaces a processing directive of the form “key=value”. Unlike the addProcessing() call, this will replace an existing processing directive for the given key value. Processing directives supported are specific to the layer type and underlying renderer.
setProjection( string proj4 ) : int
    Set the layer projection using a PROJ.4 format projection definition (ie. “+proj=utm +zone=11 +datum=WGS84” or “init=EPSG:26911”). Returns MS_SUCCESS or MS_FAILURE.
setWKTProjection( string wkt ) : int
    Set the layer projection using OpenGIS Well Known Text format. Returns MS_SUCCESS or MS_FAILURE.
whichShapes( rectObj rect ) : int
    Performs a spatial, and optionally an attribute based feature search. The function basically prepares things so that candidate features can be accessed by query or drawing functions (eg using nextShape function). Returns MS_SUCCESS, MS_FAILURE or MS_DONE. MS_DONE is returned if the layer extent does not overlap rect.

legendObj

legendObj is associated with mapObj:

+--------+ 0..1     1 +-----+
| Legend | <--------> | Map |
+--------+            +-----+

and with labelObj:

+--------+ 1        1 +-------+
| Legend | ---------> | Label |
+--------+            +-------+

legendObj Attributes

height : int
    Legend height.
imagecolor : colorObj
    Legend background color.
keysizex : int
    Width in pixels of legend keys.
keysizey : int
    Pixels.
keyspacingx : int
    Horizontal padding around keys in pixels.
keyspacingy : int
    Vertical padding.
label : labelObj immutable
    legend label.
map : mapObj immutable
    Reference to parent mapObj.
outlinecolor : colorObj
    key outline color.
position : int
    MS_UL, MS_UC, MS_UR, MS_LL, MS_LC, or MS_LR.
postlabelcache : int
    MS_TRUE or MS_FALSE.
status : int
    MS_ON, MS_OFF, or MS_EMBED.
template : string
    Path to template file.
width : int
    Label width.

legendObj Methods

None
lineObj

A lineObj is composed of one or more pointObj instances:

+------+ 0..1  1..* +-------+
| Line | ---------> | Point |
+------+            +-------+

lineObj Attributes

numpoints : int immutable
    Number of points in the line.

lineObj Methods

new lineObj( ) : lineObj
    Create a new instance.
add(pointObj point) : int
    Add point to the line. Returns MS_SUCCESS or MS_FAILURE.
get(int index) : pointObj
    Return reference to point at index.
project(projectionObj proj_in, projectionObj proj_out) : int
    Transform line in place from proj_in to proj_out. Returns MS_SUCCESS or MS_FAILURE.
set(int index, pointObj point) : int
    Set the point at index to point. Returns MS_SUCCESS or MS_FAILURE.

mapObj

A mapObj is primarily associated with instances of layerObj:

+-----+ 0..1  0..* +-------+
| Map | <--------> | Layer |
+-----+            +-------+

Secondary associations are with legendObj, scalebarObj, referenceMapObj:

+-----+ 1     0..1 +--------------+
| Map | ---------> | Legend       |
+-----+            | ------------ |
                   | Scalebar     |
                   | ------------ |
                   | ReferenceMap |
                   +--------------+

outputFormatObj:

+-----+ 1     1..* +--------------+
| Map | ---------> | OutputFormat |
+-----+            +------------- +

mapObj Attributes

cellsize : float
    Pixel size in map units.
configoptions : hashObj immutable
    A hash table of configuration options from CONFIG keywords in the .map. Direct access to config options is discouraged. Use the setConfigOption() and getConfigOption() methods instead.
datapattern : string
    TODO not sure this is meaningful for mapscript.
debug : int
    MS_TRUE or MS_FALSE.
extent : rectObj
    Map’s spatial extent.
fontset : fontSetObj immutable
    The map’s defined fonts.
height : int

    Map’s output image height in pixels.

    Note

    direct setting of height is deprecated in MapServer version 4.4. Users should set width and height simultaneously using setSize().
imagecolor : colorObj
    Initial map background color.
imagequality : int

    JPEG image quality.

    Note

    map imagequality is deprecated in MapServer 4.4 and should instead be managed through map outputformats.
imagetype : string immutable
    Name of the current output format.
interlace : int

    Output image interlacing.

    Note

    map interlace is deprecated in MapServer 4.4 and should instead be managed through map outputformats.
lablecache : labelCacheObj immutable
    Map’s labelcache.
legend : legendObj immutable
    Reference to map’s legend.
mappath : string
    Filesystem path of the map’s mapfile.
maxsize : int
    TODO ?
name : string
    Unique identifier.
numlayers : int immutable
    Number of map layers.
numoutputformats : int
    The number of output formats currently configured on the map object. Can be used to iterate over the list of output formats with the getOutputFormat(idx) method (see below).
outputformat : outputFormatObj

    The currently selected output format.

    Note

    Map outputformat should not be modified directly. Use the selectOutputFormat() method to select named formats.
outputformatlist : outputFormatObj[]

    Array of the available output formats.

    Note

    Currently only available for C#. A proper typemaps should be implemented for the other languages.

    Note

    As of 6.2 other languages can use the getoutputFormat(idx) and getNumoutputformats() functions to iterate over the format array.
querymap : queryMapObj immutable
    TODO should this be exposed to mapscript?
reference : referenceMapObj immutable
    Reference to reference map.
resolution : float
    Nominal DPI resolution. Default is 72.
scalebar : scalebarObj immutable
    Reference to the scale bar.
scaledenom : float
    The nominal map scale. A value of 25000 means 1:25000 scale.
shapepath : string
    Base filesystem path to layer data.
status : int
    MS_OFF, MS_ON, or MS_DEFAULT.
symbolset : symbolSetObj immutable
    The map’s set of symbols.
templatepattern : string
    TODO not sure this is meaningful for mapscript.
transparent : int

    MS_TRUE or MS_FALSE.

    Note

    map transparent is deprecated in MapServer 4.4 and should instead be managed through map outputformats.
units : int
    MS_DD, MS_METERS, etc.
web : webObj immutable
    Reference to map’s web definitions.
width : int

    Map’s output image width in pixels.

    Note

    direct setting of width is deprecated in MapServer version 4.4. Users should set width and height simultaneously using setSize().

mapObj Methods

new mapObj( [ string filename=’’ ] ) : mapObj
    Create a new instance of mapObj. Note that the filename is now optional.
appendOutputFormat( outputFormatObj format ) : int
    Attach format to the map’s output format list. Returns the updated number of output formats.
applyConfigOptions( ) : void
    Apply the defined configuration options set by setConfigOption().
applySLD( string sldxml ) : int
    Parse the SLD XML string sldxml and apply to map layers. Returns MS_SUCCESS or MS_FAILURE.
applySLDURL( string sldurl ) : int
    Fetch SLD XML from the URL sldurl and apply to map layers. Returns MS_SUCCESS or MS_FAILURE.
clone( ) : mapObj

    Returns a independent copy of the map, less any caches.

    Note

    In the Java module this method is named ‘cloneMap’.
draw( ) : imageObj
    Draw the map, processing layers according to their defined order and status. Return an imageObj.
drawLabelCache( imageObj image ) : int
    Draw map’s label cache on image. Returns MS_SUCCESS or MS_FAILURE.
drawLegend( ) : imageObj
    Draw map legend, returning an imageObj.
drawQuery( ) : imageObj
    Draw query map, returning an imageObj.
drawReferenceMap( ) : imageObj
    Draw reference map, returning an imageObj.
drawScalebar( ) : imageObj
    Draw scale bar, returning an imageObj.
embedLegend( imageObj image ) : int
    Embed map’s legend in image. Returns MS_SUCCESS or MS_FAILURE.
embedScalebar( imageObj image ) : int
    Embed map’s scalebar in image. Returns MS_SUCCESS or MS_FAILURE.
freeQuery( [ int qlayer=-1 ] ) : void
    Clear layer query result caches. Default is -1, or all layers.
generateSLD( ) : string
    Return SLD XML as a string for map layers that have STATUS on.
getConfigOption( string key ) : string
    Fetches the value of the requested configuration key if set. Returns NULL if the key is not set.
getFirstMetaDataKey( ) : string
    Returns the first key in the web.metadata hash table. With getNextMetaDataKey( ), provides an opaque iterator over keys.
getLabel( int labelindex ) : labelCacheMemberObj
    Return label at specified index from the map’s labelcache.
getLayer( int index ) : layerObj
    Returns a reference to the layer at index.
getLayerByName( string name ) : layerObj
    Returns a reference to the named layer.
getLayersDrawingOrder( ) : int*

    Returns an array of layer indexes in drawing order.

    Note

    Unless the proper typemap is implemented for the module’s language a user is more likely to get back an unuseable SWIG pointer to the integer array.
getMetaData( string key ) : string
    Return the value at key from the web.metadata hash table.
getNextMetaDataKey( string lastkey ) : string
    Returns the next key in the web.metadata hash table or NULL if lastkey is the last valid key. If lastkey is NULL, returns the first key of the metadata hash table.
getNumSymbols( ) : int
    Return the number of symbols in map.
getOutputFormat(int i): outputFormatObj
    Returns the output format at the specified i index from the output formats array or null if i is beyond the array bounds. The number of outpuFormats can be retrieved by calling getNumoutputformats.
getOutputFormatByName( string imagetype ) : outputFormatObj
    Return the output format corresponding to driver name imagetype or to format name imagetype. This works exactly the same as the IMAGETYPE directive in a mapfile, is case insensitive and allows an output format to be found either by driver (like ‘GD/PNG’) or name (like ‘PNG24’).
getProjection( ) : string
    Returns the PROJ.4 definition of the map’s projection.
getSymbolByName( string name ) : int

    Return the index of the named symbol in the map’s symbolset.

    Note

    This method is poorly named and too indirect. It is preferrable to use the getSymbolByName method of symbolSetObj, which really does return a symbolObj reference, or use the index method of symbolSetObj to get a symbol’s index number.
insertLayer( layerObj layer [, int nIndex=-1 ] ) : int
    Insert a copy of layer into the Map at index nIndex. The default value of nIndex is -1, which means the last possible index. Returns the index of the new Layer, or -1 in the case of a failure.
loadMapContext( string filename [, int useUniqueNames=MS_FALSE ] ) : int
    Load an OGC map context file to define extents and layers of a map.
loadOWSParameters( OWSRequest request [, string version=‘1.1.1’ ] ) : int
    Load OWS request parameters (BBOX, LAYERS, &c.) into map. Returns MS_SUCCESS or MS_FAILURE.
loadQuery( string filename ) : int
    Load a saved query. Returns MS_SUCCESS or MS_FAILURE.
moveLayerDown( int layerindex ) : int
    Move the layer at layerindex down in the drawing order array, meaning that it is drawn later. Returns MS_SUCCESS or MS_FAILURE.
moveLayerUp( int layerindex ) : int
    Move the layer at layerindex up in the drawing order array, meaning that it is drawn earlier. Returns MS_SUCCESS or MS_FAILURE.
nextLabel( ) : labelCacheMemberObj

    Return the next label from the map’s labelcache, allowing iteration over labels.

    Note

    nextLabel() is deprecated and will be removed in a future version. Replaced by getLabel().
OWSDispatch( OWSRequest req ) : int
    Processes and executes the passed OpenGIS Web Services request on the map. Returns MS_DONE (2) if there is no valid OWS request in the req object, MS_SUCCESS (0) if an OWS request was successfully processed and MS_FAILURE (1) if an OWS request was not successfully processed. OWS requests include WMS, WFS, WCS and SOS requests supported by MapServer. Results of a dispatched request are written to stdout and can be captured using the msIO services (ie. msIO_installStdoutToBuffer() and msIO_getStdoutBufferString())
prepareImage( ) : imageObj
    Returns an imageObj initialized to map extents and outputformat.
prepareQuery( ) : void
    TODO this function only calculates the scale or am I missing something?
processLegendTemplate( string names[], string values[], int numitems ) : string

    Process MapServer legend template and return HTML.

    Note

    None of the three template processing methods will be useable unless the proper typemaps are implemented in the module for the target language. Currently the typemaps are not implemented.
processQueryTemplate( string names[], string values[], int numitems ) : string

    Process MapServer query template and return HTML.

    Note

    None of the three template processing methods will be useable unless the proper typemaps are implemented in the module for the target language. Currently the typemaps are not implemented.
processTemplate( int generateimages, string names[], string values[], int numitems ) : string

    Process MapServer template and return HTML.

    Note

    None of the three template processing methods will be useable unless the proper typemaps are implemented in the module for the target language. Currently the typemaps are not implemented.
queryByFeatures( int layerindex ) : int
    Query map layers, result sets contain features that intersect or are contained within the features in the result set of the MS_LAYER_POLYGON type layer at layerindex. Returns MS_SUCCESS or MS_FAILURE.
queryByPoint( pointObj point, int mode, float buffer ) : int
    Query map layers, result sets contain one or more features, depending on mode, that intersect point within a tolerance buffer. Returns MS_SUCCESS or MS_FAILURE.
queryByRect( rectObj rect ) : int
    Query map layers, result sets contain features that intersect or are contained within rect. Returns MS_SUCCESS or MS_FAILURE.
queryByShape( shapeObj shape ) : int
    Query map layers, result sets contain features that intersect or are contained within shape. Returns MS_SUCCESS or MS_FAILURE.
removeLayer( int index ) : int
    Remove the layer at index.
removeMetaData( string key ) : int
    Delete the web.metadata hash at key. Returns MS_SUCCESS or MS_FAILURE.
removeOutputFormat( string name ) : int
    Removes the format named name from the map’s output format list. Returns MS_SUCCESS or MS_FAILURE.
save( string filename ) : int
    Save map to disk as a new map file. Returns MS_SUCCESS or MS_FAILURE.
saveMapContext( string filename ) : int
    Save map definition to disk as OGC-compliant XML. Returns MS_SUCCESS or MS_FAILURE.
saveQuery( string filename ) : int
    Save query to disk. Returns MS_SUCCESS or MS_FAILURE.
saveQueryAsGML( string filename ) : int
    Save query to disk. Returns MS_SUCCESS or MS_FAILURE.
selectOutputFormat( string imagetype ) : void
    Set the map’s active output format to the internal format named imagetype. Built-in formats are “PNG”, “PNG24”, “JPEG”, “GIF”, “GTIFF”.
setConfigOption( string key, string value ) : void
    Set the indicated key configuration option to the indicated value. Equivalent to including a CONFIG keyword in a map file.
setExtent( float minx, float miny, float maxx, float maxy ) : int
    Set the map extent, returns MS_SUCCESS or MS_FAILURE. This method will correct the extents (width/height ratio) before setting the minx,miny,maxx,maxy values. See extent properties to set up a custom extent from rectObj.
offsetExtent( float x, float y) : int
    Offset the map extent based on the given distances in map coordinates, returns MS_SUCCESS or MS_FAILURE.
scaleExtent( float zoomfactor, float minscaledenom, float maxscaledenom) : int
    Scale the map extent using the zoomfactor and ensure the extent within the minscaledenom and maxscaledenom domain. If minscaledenom and/or maxscaledenom is 0 then the parameter is not taken into account. returns MS_SUCCESS or MS_FAILURE.
setCenter( pointObj center ) : int
    Set the map center to the given map point, returns MS_SUCCESS or MS_FAILURE.
setFontSet( string filename ) : int
    Load fonts defined in filename into map fontset. The existing fontset is cleared. Returns MS_SUCCESS or MS_FAILURE.
setImageType( string name ) : void

    Sets map outputformat to the named format.

    Note

    setImageType() remains in the module but it’s use is deprecated in favor of selectOutputFormat().
setLayersDrawingOrder( int layerindexes[]) : int

    Set map layer drawing order.

    Note

    Unless the proper typemap is implemented for the module’s language users will not be able to pass arrays or lists to this method and it will be unusable.
setMetaData( string key, string value ) : int
    Assign value to the web.metadata hash at key. Return MS_SUCCESS or MS_FAILURE.
setOutputFormat( outputFormatObj format ) : void
    Sets map outputformat.
setProjection( string proj4 ) : int
    Set map projection from PROJ.4 definition string proj4.
setRotation( float rotation_angle ) : int
    Set map rotation angle. The map view rectangle (specified in EXTENTS) will be rotated by the indicated angle in the counter- clockwise direction. Note that this implies the rendered map will be rotated by the angle in the clockwise direction. Returns MS_SUCCESS or MS_FAILURE.
setSize( int width, int height ) : int
    Set map’s image width and height together and carry out the necessary subsequent geotransform computation. Returns MS_SUCCESS or MS_FAILURE.
setSymbolSet( string filename ) : int
    Load symbols defined in filename into map symbolset. The existing symbolset is cleared. Returns MS_SUCCESS or MS_FAILURE.
setWKTProjection( string wkt ) : int
    Sets map projection from OGC definition wkt.
zoomPoint( int zoomfactor, pointObj imgpoint, int width, int height, rectObj extent, rectObj maxextent ) : int
    Zoom by zoomfactor to imgpoint in pixel units within the image of height and width dimensions and georeferenced extent. Zooming can be constrained to a maximum maxextent. Returns MS_SUCCESS or MS_FAILURE.
zoomRectangle( rectObj imgrect, int width, int height, rectObj extent,

    rectObj maxextent ) : int Zoom to a pixel coordinate rectangle in the image of width and height dimensions and georeferencing extent. Zooming can be constrained to a maximum maxextent. The imgrect rectangle contains the coordinates of the LL and UR coordinates in pixel: the maxy in the rect object should be < miny value. Returns MS_SUCCESS or MS_FAILURE:

    ------- UR (values in the rect object : maxx, maxy)
    |     |
    |     |
    |     |
    ------
    LL (values in the rectobject minx, miny)

zoomScale( float scale, pointObj imgpoint, int width, int height, rectObj extent, rectObj maxextent) : int
    Like the previous methods, but zooms to the point at a specified scale.

markerCacheMemberObj

An individual marker. The markerCacheMemberObj class is associated with labelCacheObj:

+------------------+ 0..*     1 +------------+
| MarkerCacheMember | <--------- | LabelCache |
+------------------+            +------------+

markerCacheMemberObj Attributes

id : int immutable
    Id of the marker.
poly : shapeObj immutable
    Marker bounding box.

markerCacheMemberObj Methods

None.
outputFormatObj

An outputFormatObj is associated with a mapObj:

+--------------+ 1..*     1 +-----+
| OutputFormat | <--------- | Map |
+--------------+            +-----+

and can also be an attribute of an imageObj.
outputFormatObj Attributes

bands : int
    The number of bands in the raster. Only used for the “raw” modes, MS_IMAGEMODE_BYTE, MS_IMAGEMODE_INT16, and MS_IMAGEMODE_FLOAT32. Normally set via the BAND_COUNT formatoption ... this field should be considered read-only.
driver : string
    A string such as ‘GD/PNG’ or ‘GDAL/GTiff’.
extension : string
    Format file extension such as ‘png’.
imagemode : int
    MS_IMAGEMODE_PC256, MS_IMAGEMODE_RGB, MS_IMAGEMODE_RGBA, MS_IMAGEMODE_INT16, MS_IMAGEMODE_FLOAT32, MS_IMAGEMODE_BYTE, or MS_IMAGEMODE_NULL.
mimetype : string
    Format mimetype such as ‘image/png’.
name : string
    A unique identifier.
numformatoptions: int
    The number of option values set on this format. Can be used to iterate over the options array in conjunction with getOptionAt
renderer : int
    MS_RENDER_WITH_GD, MS_RENDER_WITH_SWF, MS_RENDER_WITH_RAWDATA, MS_RENDER_WITH_PDF, or MS_RENDER_WITH_IMAGEMAP. Normally set internally based on the driver and some other setting in the constructor.
transparent : int
    MS_ON or MS_OFF.

outputFormatObj Methods

new outputFormatObj( string driver [, string name=driver ] ) : outputFormatObj
    Create new instance. If name is not provided, the value of driver is used as a name.
getOption( string key [, string defaultvalue=”” ] ) : string
    Return the format option at key or defaultvalue if key is not a valid hash index.
getOptionAt(int idx): string
    Returns the option at idx or null if the index is beyond the array bounds. The option is returned as the original KEY=VALUE string. The number of available options can be obtained by calling getNumformatoptions.
setExtension( string extension ) : void
    Set file extension for output format such as ‘png’ or ‘jpg’. Method could probably be deprecated since the extension attribute is mutable.
setMimetype( string mimetype ) : void
    Set mimetype for output format such as ‘image/png’ or ‘image/jpeg’. Method could probably be deprecated since the mimetype attribute is mutable.
setOption( string key, string value ) : void
    Set the format option at key to value. Format options are mostly driver specific.
validate() : int
    Checks some internal consistency issues, and returns MS_TRUE if things are OK and MS_FALSE if there are problems. Some problems are fixed up internally. May produce debug output if issues encountered.

OWSRequest

Not associated with other mapscript classes. Serves as a message intermediary between an application and MapServer’s OWS capabilities. Using it permits creation of lightweight WMS services:

wms_map = mapscript.mapObj('wms.map')
wms_request = mapscript.OWSRequest()

# Convert application request parameters (req.args)
for param, value in req.args.items():
    wms_request.setParam(param, value)

# Map loads parameters from OWSRequest, adjusting its SRS, extents,
# active layers accordingly
wms_map.loadWMSRequest('1.1.0', wms_request)

# Render the Map
img = wms_map.draw()

OWSRequest Attributes

NumParams : int immutable
    Number of request parameters. Eventually should be changed to numparams lowercase like other attributes.
postrequest : string
    TODO
type : int
    MS_GET_REQUEST or MS_POST_REQUEST.

OWSRequest Methods

new OWSRequest( ) : OWSRequest

    Create a new instance.

    Note

    MapServer’s OWSRequest supports only single valued parameters.
addParameter( string name, string value ) : void

    Add a request parameter, even if the parameter key was previousely set. This is useful when multiple parameters with the same key are required. For example:

    request.addParameter('SIZE', 'x(100)')
    request.addParameter('SIZE', 'y(100)')

getName( int index ) : string
    Return the name of the parameter at index in the request’s array of parameter names.
getValue( int index ) : string
    Return the value of the parameter at index in the request’s array of parameter values.
getValueByName( string name) : string
    Return the value associated with the parameter name.
loadParams() : int
    Initializes the OWSRequest object from the cgi environment variables REQUEST_METHOD, QUERY_STRING and HTTP_COOKIE. Returns the number of name/value pairs collected. Warning: most errors will result in a process exit!
loadParamsFromURL( string url ) : int
    Initializes the OWSRequest object from the provided URL which is treated like a QUERY_STRING. Note that REQUEST_METHOD=GET and no post data is assumed in this case. This method was added in MapServer 6.0.
setParameter( string name, string value ) : void

    Set a request parameter. For example:

    request.setParameter('REQUEST', 'GetMap')
    request.setParameter('BBOX', '-107.0,40.0,-106.0,41.0')

pointObj

A pointObj instance may be associated with a lineObj:

+-------+ 1..*  0..1 +------+
| Point | <--------- | Line |
+-------+            +------+

pointObj Attributes

m : float
    Measure. Meaningful only for measured shapefiles. Given value -2e38 if not otherwise assigned to indicate “nodata”.
x : float
    Easting
y : float
    Northing
z : float
    Elevation

pointObj Methods

new pointObj( [ float x=0.0, float y=0.0, float z=0.0, float m=-2e38 ] ) : pointObj
    Create new instance. Easting, northing, and measure arguments are optional.
distanceToPoint( pointObj point ) : float
    Returns the distance to point.
distanceToSegment( pointObj point1, pointObj point2 ) : float
    Returns the minimum distance to a hypothetical line segment connecting point1 and point2.
distanceToShape( shapeObj shape ) : float
    Returns the minimum distance to shape.
draw( mapObj map, layerObj layer, imageObj image, int classindex, string text ) : int
    Draw the point using the styles defined by the classindex class of layer and labeled with string text. Returns MS_SUCCESS or MS_FAILURE.
project( projectionObj proj_in, projectionObj proj_out ) : int
    Reproject point from proj_in to proj_out. Transformation is done in place. Returns MS_SUCCESS or MS_FAILURE.
setXY( float x, float y [, float m=2e-38 ] ) : int
    Set spatial coordinate and, optionally, measure values simultaneously. The measure will be set only if the value of m is greater than the ESRI measure no-data value of 1e-38. Returns MS_SUCCESS or MS_FAILURE.
setXYZ( float x, float y, float z [, float m=-2e38 ] ) : int
    Set spatial coordinate and, optionally, measure values simultaneously. The measure will be set only if the value of m is greater than the ESRI measure no-data value of -1e38. Returns MS_SUCCESS or MS_FAILURE.
setXYZM( float x, float y, float z, float m ) : int
    Set spatial coordinate and, optionally, measure values simultaneously. The measure will be set only if the value of m is greater than the ESRI measure no-data value of -1e38. Returns MS_SUCCESS or MS_FAILURE.
toShape() : shapeObj
    Convience method to quickly turn a point into a shapeObj.
toString() : string

    Return a string formatted like:

    { 'x': %f , 'y': %f, 'z': %f }

    with the coordinate values substituted appropriately. Python users can get the same effect via the pointObj __str__ method:

    >>> p = mapscript.pointObj(1, 1)
    >>> str(p)
    { 'x': 1.000000 , 'y': 1.000000, 'z': 1.000000 }

projectionObj

This class is not really fully implemented yet. MapServer’s Maps and Layers have Projection attributes, and these are C projectionObj structures, but are not directly exposed by the mapscript module. Currently we have to do some round-a-bout logic like this:

point.project(projectionObj(mapobj.getProjection(),
              projectionObj(layer.getProjection())

to project a point from map to layer reference system.
projectionObj Attributes

numargs : int immutable
    Number of PROJ.4 arguments.

projectionObj Methods

new projectionObj( string proj4 ) : projectionObj
    Create new instance of projectionObj. Input parameter proj4 is a PROJ.4 definition string such as “init=EPSG:4269”.
getUnits() : int
    Returns the units of a projection object. Returns -1 on error.

rectObj

A rectObj may be a lone object or an attribute of another object and has no other associations.
rectObj Attributes

maxx : float
    Maximum easting
maxy : float
    Maximum northing
minx : float
    Minimum easting
miny : float
    Minimum northing

rectObj Methods

new rectObj( [ float minx=-1.0, float miny=-1.0, float maxx=-1.0, float maxy=-1.0, int imageunits=MS_FALSE ] ) : rectObj
    Create new instance. The four easting and northing arguments are optional and default to -1.0. Note the new optional fifth argument which allows creation of rectangles in image (pixel/line) units which are also tested for validity.
draw( mapObj map, layerObj layer, imageObj img, int classindex, string text ) : int
    Draw rectangle into img using style defined by the classindex class of layer. The rectangle is labeled with the string text. Returns MS_SUCCESS or MS_FAILURE.
getCenter() : pointObj
    Return the center point of the rectagle.
project( projectionObj proj_in, projectionObj proj_out ) : int
    Reproject rectangle from proj_in to proj_out. Transformation is done in place. Returns MS_SUCCESS or MS_FAILURE.
toPolygon() : shapeObj
    Convert to a polygon of five vertices.
toString() : string

    Return a string formatted like:

    { 'minx': %f , 'miny': %f , 'maxx': %f , 'maxy': %f }

    with the bounding values substituted appropriately. Python users can get the same effect via the rectObj __str__ method:

    >>> r = mapscript.rectObj(0, 0, 1, 1)
    >>> str(r)
    { 'minx': 0 , 'miny': 0 , 'maxx': 1 , 'maxy': 1 }

referenceMapObj

A referenceMapObj is associated with mapObj:

+--------------+ 0..1     1 +-----+
| ReferenceMap | <--------> | Map |
+--------------+            +-----+

referenceMapObj Attributes

color : colorObj
    Color of reference box.
extent : rectObj
    Spatial extent of reference in units of parent map.
height : int
    Height of reference map in pixels.
image : string
    Filename of reference map image.
map : mapObj immutable
    Reference to parent mapObj.
marker : int
    Index of a symbol in the map symbol set to use for marker.
markername : string
    Name of a symbol.
markersize : int
    Size of marker.
maxboxsize : int
    Pixels.
minboxsize : int
    Pixels.
outlinecolor : colorObj
    Outline color of reference box.
status : int
    MS_ON or MS_OFF.
width : int
    In pixels.

referenceMapObj Methods

None
resultCacheMemberObj

Has no associations with other MapScript classes and has no methods. By using several indexes, a resultCacheMemberObj refers to a single layer feature.
resultCacheMemberObj Attributes

classindex : int immutable
    The index of the layer class into which the feature has been classified.
shapeindex : int immutable
    Index of the feature within the layer.
tileindex : int immutable
    Meaningful for tiled layers only, index of the shapefile data tile.

resultCacheObj

See querying-HOWTO.txt for extra guidance in using the new 4.4 query API.
resultCacheObj Attributes

bounds : rectObj immutable
    Bounding box of query results.
numresults : int immutable
    Length of result set.

resultCacheObj Methods

getResult( int i ) : resultCacheMemberObj
    Returns the result at index i, like layerObj::getResult, or NULL if index is outside the range of results.

scalebarObj

A scalebarObj is associated with mapObj:

+----------+ 0..1     1 +-----+
| Scalebar | <--------- | Map |
+----------+            +-----+

and also with labelObj:

+----------+ 1        1 +-------+
| Scalebar | ---------> | Label |
+----------+            +-------+

scalebarObj Attributes

backgroundcolor : colorObj
    Scalebar background color.
color : colorObj
    Scalebar foreground color.
height : int
    Pixels.
imagecolor : colorObj
    Background color of scalebar.
intervals : int
    Number of intervals.
label : labelObj
    Scalebar label.
outlinecolor : colorObj
    Foreground outline color.
position : int
    MS_UL, MS_UC, MS_UR, MS_LL, MS_LC, or MS_LR.
postlabelcache : int
    MS_TRUE or MS_FALSE.
status : int
    MS_ON, MS_OFF, or MS_EMBED.
style : int
    0 or 1.
units : int
    See MS_UNITS in mapserver.h.
width : int
    Pixels.

scalebarObj Methods

None
shapefileObj
shapefileObj Attributes

bounds : rectObj
    Extent of shapes.
numshapes : int
    Number of shapes.
type : int
    See mapshape.h for values of type.

shapefileObj Methods

new shapefileObj( string filename [, int type=-1 ] ) : shapefileObj
    Create a new instance. Omit the type argument or use a value of -1 to open an existing shapefile.
add( shapeObj shape ) : int
    Add shape to the shapefile. Returns MS_SUCCESS or MS_FAILURE.
get( int i, shapeObj shape ) : int
    Get the shapefile feature from index i and store it in shape. Returns MS_SUCCESS or MS_FAILURE.
getShape( int i ) : shapeObj
    Returns the shapefile feature at index i. More effecient than get.

TODO
shapeObj

Each feature of a layer’s data is a shapeObj. Each part of the shape is a closed lineObj:

+-------+ 1    1..* +------+
| Shape | --------> | Line |
+-------+           +------+

shapeObj Attributes

bounds : rectObj
    Bounding box of shape.
classindex : int
    The class index for features of a classified layer.
index : int
    Feature index within the layer.
numlines : int immutable
    Number of parts.
numvalues : int immutable
    Number of shape attributes.
text : string
    Shape annotation.
tileindex : int
    Index of tiled file for tileindexed layers.
type : int
    MS_SHAPE_POINT, MS_SHAPE_LINE, MS_SHAPE_POLYGON, or MS_SHAPE_NULL.

shapeObj Methods

new shapeObj( int type ) : shapeObj
    Return a new shapeObj of the specified type. See the type attribute above. No attribute values created by default. initValues should be explicitly called to create the required number of values.
add( lineObj line ) : int
    Add line (i.e. a part) to the shape. Returns MS_SUCCESS or MS_FAILURE.
boundary() : shapeObj
    Returns the boundary of the existing shape. Requires GEOS support. Returns NULL/undef on failure.
buffer( int distance ) : shapeObj
    Returns a new buffered shapeObj based on the supplied distance (given in the coordinates of the existing shapeObj). Requires GEOS support. Returns NULL/undef on failure.
clone() : shapeObj
    Return an independent copy of the shape.
contains( pointObj point ) : int
    Returns MS_TRUE if the point is inside the shape, MS_FALSE otherwise.
contains( shapeObj shape2 ) : int
    Returns MS_TRUE if shape2 is entirely within the shape. Returns -1 on error and MS_FALSE otherwise. Requires GEOS support.
convexHull() : shapeObj
    Returns the convex hull of the existing shape. Requires GEOS support. Returns NULL/undef on failure.
copy( shapeObj shape_copy ) : int
    Copy the shape to shape_copy. Returns MS_SUCCESS or MS_FAILURE.
crosses( shapeObj shape2 ) : int
    Returns MS_TRUE if shape2 crosses the shape. Returns -1 on error and MS_FALSE otherwise. Requires GEOS support.
difference( shapeObj shape ) : shapeObj
    Returns the computed difference of the supplied and existing shape. Requires GEOS support. Returns NULL/undef on failure.
disjoint( shapeObj shape2 ) : int
    Returns MS_TRUE if shape2 and the shape are disjoint. Returns -1 on error and MS_FALSE otherwise. Requires GEOS support.
distanceToPoint( pointObj point ) : float
    Return distance to point.
distanceToShape( shapeObj shape ) : float
    Return the minimum distance to shape.
draw( mapObj map, layerObj layer, imageObj img ) : int
    Draws the individual shape using layer. Returns MS_SUCCESS or MS_FAILURE.
equals( shapeObj shape2 ) : int
    Returns MS_TRUE if the shape and shape2 are equal (geometry only). Returns -1 on error and MS_FALSE otherwise. Requires GEOS support.
fromWKT( char \*wkt ) : shapeObj
    Returns a new shapeObj based on a well-known text representation of a geometry. Requires GEOS support. Returns NULL/undef on failure.
get( int index ) : lineObj
    Returns a reference to part at index. Reference is valid only during the life of the shapeObj.
getArea() : double
    Returns the area of the shape (if applicable). Requires GEOS support.
getCentroid() : pointObj
    Returns the centroid for the existing shape. Requires GEOS support. Returns NULL/undef on failure.
getLength() : double
    Returns the length (or perimeter) of a shape. Requires GEOS support.
getValue( int i ) : string
    Return the shape attribute at index i.
initValues( int numvalues ) : void
    Allocates memory for the requested number of values.
intersects( shapeObj shape ) : int

    Returns MS_TRUE if the two shapes intersect, MS_FALSE otherwise.

    Note

    Does not require GEOS support but will use GEOS functions if available.
intersection( shapeObj shape ) : shapeObj
    Returns the computed intersection of the supplied and existing shape. Requires GEOS support. Returns NULL/undef on failure.
overlaps( shapeObj shape2 ) : int
    Returns MS_TRUE if shape2 overlaps shape. Returns -1 on error and MS_FALSE otherwise. Requires GEOS support.
project( projectionObj proj_in, projectionObj proj_out ) : int
    Reproject shape from proj_in to proj_out. Transformation is done in place. Returns MS_SUCCESS or MS_FAILURE.
setBounds : void

    Must be called to calculate new bounding box after new parts have been added.

    TODO: should return int and set msSetError.
setValue( int i, string value ) : int
    Set the shape value at index i to value.
simplify( double tolerance ): shapeObj
    Given a tolerance, returns a simplified shape object or NULL on error. Requires GEOS support (>=3.0).
symDifference( shapeObj shape ) : shapeObj
    Returns the computed symmetric difference of the supplied and existing shape. Requires GEOS support. Returns NULL/undef on failure.
topologySimplifyPreservingSimplify( double tolerance ): shapeObj
    Given a tolerance, returns a simplified shape object or NULL on error. Requires GEOS support (>=3.0).
touches( shapeObj shape2 ) : int
    Returns MS_TRUE if the shape and shape2 touch. Returns -1 on error and MS_FALSE otherwise. Requires GEOS support.
toWKT() : string
    Returns the well-known text representation of a shapeObj. Requires GEOS support. Returns NULL/undef on failure.
Union( shapeObj shape ) : shapeObj
    Returns the union of the existing and supplied shape. Shapes must be of the same type. Requires GEOS support. Returns NULL/undef on failure.
within( shapeObj shape2 ) : int
    Returns MS_TRUE if the shape is entirely within shape2. Returns -1 on error and MS_FALSE otherwise. Requires GEOS support.

styleObj

An instance of styleObj is associated with one instance of classObj:

+-------+ 0..*    1 +-------+
| Style | <-------- | Class |
+-------+           +-------+

An instance of styleObj can exist outside of a classObj container and be explicitly inserted into the classObj for use in mapping:

new_style = new styleObj()
the_class.insertStyle(new_style)

It is important to understand that insertStyle inserts a copy of the styleObj instance, not a reference to the instance itself.

The older use case:

new_style = new styleObj(the_class)

remains supported. These will be the only ways to access the styles of a class. Programmers should no longer directly access the styles attribute.
styleObj Attributes

angle : double
    Angle, given in degrees, to draw the line work. Default is 0. For symbols of Type HATCH, this is the angle of the hatched lines.
angleitem : string

    Deprecated since version 5.0: Use setBinding.
antialias : int
    MS_TRUE or MS_FALSE. Should TrueType fonts be antialiased.
backgroundcolor : colorObj
    Background pen color.
color : colorObj
    Foreground or fill pen color.
mincolor : colorObj
    Attribute for Color Range Mapping (MS RFC 6: Color Range Mapping of Continuous Feature Values). mincolor, minvalue, maxcolor, maxvalue define the range for mapping a continuous feature value to a continuous range of colors when rendering the feature on the map.
minsize : int
    Minimum pen or symbol width for scaling styles.
minvalue : double
    Attribute for Color Range Mapping (MS RFC 6: Color Range Mapping of Continuous Feature Values). mincolor, minvalue, maxcolor, maxvalue define the range for mapping a continuous feature value to a continuous range of colors when rendering the feature on the map.
minwidth : int
    Minimum width of the symbol.
maxcolor : colorObj
    Attribute for Color Range Mapping (MS RFC 6: Color Range Mapping of Continuous Feature Values). mincolor, minvalue, maxcolor, maxvalue define the range for mapping a continuous feature value to a continuous range of colors when rendering the feature on the map.
maxsize : int
    Maximum pen or symbol width for scaling.
maxvalue : double
    Attribute for Color Range Mapping (MS RFC 6: Color Range Mapping of Continuous Feature Values). mincolor, minvalue, maxcolor, maxvalue define the range for mapping a continuous feature value to a continuous range of colors when rendering the feature on the map.
maxwidth : int
    Maximum width of the symbol.
offsetx : int
    Draw with pen or symbol offset from map data.
offsety : int
    Draw with pen or symbol offset from map data.
outlinecolor : colorObj
    Outline pen color.
rangeitem : string
    Attribute/field that stores the values for the Color Range Mapping (MS RFC 6: Color Range Mapping of Continuous Feature Values).
size : int
    Pixel width of the style’s pen or symbol.
sizeitem : string

    Deprecated since version 5.0: Use setBinding.
symbol : int
    The index within the map symbolset of the style’s symbol.
symbolname : string immutable
    Name of the style’s symbol.
width : int
    Width refers to the thickness of line work drawn, in pixels. Default is 1. For symbols of Type HATCH, the with is how thick the hatched lines are.

styleObj Methods

new styleObj( [ classObj parent_class ] ) : styleObj
    Returns new default style Obj instance. The parent_class is optional.
clone : styleObj
    Returns an independent copy of the style with no parent class.
getBinding( int binding ) : string
    Get the attribute binding for a specified style property. Returns NULL if there is no binding for this property.
removeBinding( int binding ) : int
    Remove the attribute binding for a specfiled style property.
setBinding ( int binding, string item ) : int

    Set the attribute binding for a specified style property. Binding constants look like this: MS_STYLE_BINDING_[attribute name]:

    setBinding(MS_STYLE_BINDING_SIZE, 'mySizeItem');

setSymbolByName(mapObj map, string symbolname) : int
    Setting the symbol of the styleObj given the reference of the map object and the symbol name.
updateFromString ( string snippet ) : int
    Update a style from a string snippet. Returns MS_SUCCESS/MS_FAILURE.

symbolObj

A symbolObj is associated with one symbolSetObj:

+--------+ 0..*    1 +-----------+
| Symbol | <-------- | SymbolSet |
+--------+           +-----------+

A styleObj will often refer to a symbolObj by name or index, but this is not really an object association, is it?
symbolObj Attributes

antialias : int
    MS_TRUE or MS_FALSE.
character : string
    For TrueType symbols.
filled : int
    MS_TRUE or MS_FALSE.
font : string
    For TrueType symbols.
gap : int
    Moved to STYLE
imagepath : string
    Path to pixmap file.
inmapfile : int
    If set to TRUE, the symbol will be saved inside the mapfile. Added in MapServer 5.6.1
linecap : int
    Moved to STYLE
linejoin : int
    Moved to STYLE
linejoinmaxsize : float
    Moved to STYLE
name : string
    Symbol name
numpoints : int immutable
    Number of points of a vector symbol.
position : int
    No more available?
sizex : float
    TODO what is this?
sizey : float
    TODO what is this?
stylelength : int
    Number of intervals
transparent : int
    TODO what is this?
transparentcolor : int
    TODO is this a derelict attribute?
type : int
    MS_SYMBOL_SIMPLE, MS_SYMBOL_VECTOR, MS_SYMBOL_ELLIPSE, MS_SYMBOL_PIXMAP, or MS_SYMBOL_TRUETYPE.

symbolObj Methods

new symbolObj( string symbolname [, string imagefile ] ) : symbolObj
    Create new default symbol named name. If imagefile is specified, then the symbol will be of type MS_SYMBOL_PIXMAP.
getImage() : imageObj
    Returns a pixmap symbol’s imagery as an imageObj.
getPoints() : lineObj
    Returns the symbol points as a lineObj.
setImage( imageObj image ) : int
    Set a pixmap symbol’s imagery from image.
setPoints( lineObj line ) : int
    Sets the symbol points from the points of line. Returns the updated number of points.
setStyle( int index, int value ) : int
    Set the style at index to value. Returns MS_SUCCESS or MS_FAILURE.

symbolSetObj

A symbolSetObj is an attribute of a mapObj and is associated with instances of symbolObj:

+-----------+ 1    0..* +--------+
| SymbolSet | --------> | Symbol |
+-----------+           +--------+

symbolSetObj Attributes

filename : string
    Symbolset filename
numsymbols : int immutable
    Number of symbols in the set.

symbolSetObj Methods

new symbolSetObj( [ string symbolfile ] ) : symbolSetObj
    Create new instance. If symbolfile is specified, symbols will be loaded from the file.
appendSymbol( symbolObj symbol ) : int
    Add a copy of symbol to the symbolset and return its index.
getSymbol( int index ) : symbolObj
    Returns a reference to the symbol at index.
getSymbolByName( string name ) : symbolObj
    Returns a reference to the symbol named name.
index( string name ) : int
    Return the index of the symbol named name or -1 in the case that no such symbol is found.
removeSymbol( int index ) : symbolObj
    Remove the symbol at index and return a copy of the symbol.
save( string filename ) : int
    Save symbol set to a file. Returns MS_SUCCESS or MS_FAILURE.

webObj

Has no other existence than as an attribute of a mapObj. Serves as a container for various run-time web application definitions like temporary file paths, template paths, etc.
webObj Attributes

empty : string
    TODO
error : string
    TODO
extent : rectObj
    Clipping extent.
footer : string
    Path to footer document.
header : string
    Path to header document.
imagepath : string
    Filesystem path to temporary image location.
imageurl : string
    URL to temporary image location.
log : string
    TODO
map : mapObj immutable
    Reference to parent mapObj.
maxscaledenom : float
    Minimum map scale.
maxtemplate : string
    TODO
metadata : hashTableObj immutable
    metadata hash table.
minscaledenom : float
    Maximum map scale.
mintemplate : string
    TODO
queryformat : string
    TODO
template : string
    Path to template document.

webObj Methods

None.

