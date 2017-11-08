# coding: utf-8
from sqlalchemy import (Boolean, Column, Float, Index, Integer,
                        LargeBinary, Numeric, Table, Text, text)
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AbTest(Base):
    __tablename__ = 'AbTest'

    Id = Column(Text, primary_key=True)
    Expiration = Column(Text)
    Name = Column(Text)
    GroupId = Column(Integer)
    Variables = Column(Text)
    Status = Column(Integer)
    Description = Column(Text)
    Checksum = Column(Text)
    TestKey = Column(Text)


class Achievement(Base):
    __tablename__ = 'Achievement'

    Acknowledged = Column(Boolean)
    CompleteDescription = Column(Text)
    DateCreated = Column(Text)
    Difficulty = Column(Integer)
    EventLogDescription = Column(Text)
    Hidden = Column(Boolean)
    Id = Column(Text, primary_key=True)
    ImageId = Column(Text, nullable=False)
    IncompleteDescription = Column(Text)
    Name = Column(Text, nullable=False)
    Ordinal = Column(Integer)
    PercentComplete = Column(Integer)
    Presented = Column(Boolean)
    Synchronized = Column(Boolean)
    UserId = Column(Text)
    Checksum = Column(Text)
    FacebookImageId = Column(Text)


class Activity(Base):
    __tablename__ = 'Activity'

    Id = Column(Text, primary_key=True, nullable=False, index=True)
    Enabled = Column(Numeric, server_default=text("TRUE"))
    Type = Column(Text, primary_key=True, nullable=False)
    Action = Column(Integer)
    Date = Column(Text)
    Data = Column(LargeBinary)


class AnalyticsEvent(Base):
    __tablename__ = 'AnalyticsEvents'

    Id = Column(Text, primary_key=True)
    Type = Column(Text)
    Timestamp = Column(Text, index=True)
    Attributes = Column(Text)
    Metrics = Column(Text)
    TestGroups = Column(Text)
    ClientApplicationVersion = Column(Text)


class Author(Base):
    __tablename__ = 'Authors'

    UserId = Column(Text, primary_key=True)
    Avatar = Column(Text)
    Name = Column(Text)
    FacebookId = Column(Text)


class BookAuthor(Base):
    __tablename__ = 'BookAuthors'

    AuthorId = Column(Text, primary_key=True, nullable=False)
    BookId = Column(Text, primary_key=True, nullable=False)


class Bookmark(Base):
    __tablename__ = 'Bookmark'

    BookmarkID = Column(Text, primary_key=True)
    VolumeID = Column(Text, nullable=False)
    ContentID = Column(Text, nullable=False, index=True)
    StartContainerPath = Column(Text, nullable=False)
    StartContainerChildIndex = Column(Integer, nullable=False)
    StartOffset = Column(Integer, nullable=False)
    EndContainerPath = Column(Text, nullable=False)
    EndContainerChildIndex = Column(Integer, nullable=False)
    EndOffset = Column(Integer, nullable=False)
    Text = Column(Text)
    Annotation = Column(Text)
    ExtraAnnotationData = Column(LargeBinary)
    DateCreated = Column(Text)
    ChapterProgress = Column(Float, nullable=False, server_default=text("0"))
    Hidden = Column(Boolean, nullable=False, server_default=text("0"))
    Version = Column(Text)
    DateModified = Column(Text)
    Creator = Column(Text)
    UUID = Column(Text)
    UserID = Column(Text)
    SyncTime = Column(Text)
    Published = Column(Numeric, server_default=text("false"))


class DbVersion(Base):
    __tablename__ = 'DbVersion'

    version = Column(Integer, primary_key=True)


class Dictionary(Base):
    __tablename__ = 'Dictionary'

    Suffix = Column(Text, primary_key=True)
    Name = Column(Text)
    Installed = Column(Boolean)
    Size = Column(Text)
    LastModified = Column(Text)
    IsSynced = Column(Boolean)


class Content(Base):
    __tablename__ = 'content'

    """
        description: uuids for books; file paths for chapters
                if book not a kobo entry, then uses file path
        examples:
             13204fd1-571b-43c7-97e4-e368399eb324: designates a book id
            /mnt/onboard/.kobo/kepub/1b67cdf8-fc1d-429b-b8d1-89dc44d25889!OEBPS!c/c6.html#i6: a chapter
        """
    ContentID = Column(Text, primary_key=True)

    """
    observed: 6, 9, 899
        6: books
        9: chapters within books
        899: ?? possibly also chapter markers
    """
    ContentType = Column(Text, nullable=False)

    """
    description: describes file type
    observed: application/x-kobo-epub+zip, application/pdf, application/epub+zip,
          application/xhtml+xml, application/x-cbz

    """
    MimeType = Column(Text, nullable=False)

    """
    description: acts as a uuid for book on a chapter row; null on books
    """
    BookID = Column(Text, index=True)

    """
    description: acts as the Title for book on a chapter row; null on books
    """
    BookTitle = Column(Text)

    """
    description: for books, maps to image stored in .kobo/images; null on chapters
    """
    ImageId = Column(Text)

    """
    description: book title if book, chapter title if chapter
    """
    Title = Column(Text, index=True)

    """
    description: book author, if book; null on chapters
    """
    Attribution = Column(Text, index=True)

    """
    description: the html formatted description of the book; null on chapters
    """
    Description = Column(Text)

    """
    description: date the book was added to my account; null if chapters
    example: 2016-02-21T05:00:00.000
    """
    DateCreated = Column(Text)
    ShortCoverKey = Column(Text)
    adobe_location = Column(Text)
    Publisher = Column(Text)
    IsEncrypted = Column(Boolean)
    DateLastRead = Column(Text, index=True)
    FirstTimeReading = Column(Boolean)
    ChapterIDBookmarked = Column(Text)
    ParagraphBookmarked = Column(Integer)
    BookmarkWordOffset = Column(Integer)
    NumShortcovers = Column(Integer)
    VolumeIndex = Column(Integer)
    ___NumPages = Column(Integer)

    """
    observed: 0, 1, 2, 3
        0: Unread
        1: In Progress/Currently Reading
        2: Read
        3: Closed/Removed
    """
    ReadStatus = Column(Integer)
    ___SyncTime = Column(Text)

    """
    description: mostly a foreign key to UserID
    observed: user_id uuid, 'removed', 'adobe_user'
        user_id uuid: seem to be all active items associated with my account
        'removed': ??
        'adobe_user': used with "Kobo eReader User Guide" and any adobe digital editions
    """
    ___UserID = Column(Text, nullable=False)
    PublicationId = Column(Text)
    ___FileOffset = Column(Integer)
    ___FileSize = Column(Integer)
    ___PercentRead = Column(Integer)

    """
    description: whether the book was removed locally; null for chapters
    observed: 0, 3
        0: book exists locally
        3: book was removed
    """
    ___ExpirationStatus = Column(Integer)
    FavouritesIndex = Column(NullType, nullable=False, server_default=text("-1"))

    """
    observed: 0, 1, 3, 6, -1
    """
    Accessibility = Column(Integer, server_default=text("1"))
    ContentURL = Column(Text)
    Language = Column(Text)
    BookshelfTags = Column(Text)
    IsDownloaded = Column(Numeric, nullable=False, server_default=text("1"))
    FeedbackType = Column(Integer, server_default=text("0"))
    AverageRating = Column(Integer, server_default=text("0"))
    Depth = Column(Integer)
    PageProgressDirection = Column(Text)
    InWishlist = Column(Boolean, nullable=False, server_default=text("FALSE"))
    ISBN = Column(Text)
    WishlistedDate = Column(Text, server_default=text("0000-00-00T00:00:00.000"))
    FeedbackTypeSynced = Column(Integer, server_default=text("0"))
    IsSocialEnabled = Column(Boolean, nullable=False, server_default=text("TRUE"))
    EpubType = Column(Integer, nullable=False, server_default=text("-1"))
    Monetization = Column(Integer, server_default=text("2"))
    ExternalId = Column(Text)
    Series = Column(Text)
    SeriesNumber = Column(Text)
    Subtitle = Column(Text)
    WordCount = Column(Integer, server_default=text("-1"))
    Fallback = Column(Text)
    RestOfBookEstimate = Column(Integer)
    CurrentChapterEstimate = Column(Integer)
    CurrentChapterProgress = Column(Float)
    PocketStatus = Column(Integer, server_default=text("0"))
    UnsyncedPocketChanges = Column(Text)
    ImageUrl = Column(Text)
    DateAdded = Column(Text)
    WorkId = Column(Text)
    Properties = Column(Text)
    RenditionSpread = Column(Text)
    RatingCount = Column(Integer, server_default=text("0"))
    ReviewsSyncDate = Column(Text)
    MediaOverlay = Column(Text)
    MediaOverlayType = Column(Text)
    RedirectPreviewUrl = Column(Text)
    PreviewFileSize = Column(Integer)
    EntitlementId = Column(Text)
    CrossRevisionId = Column(Text)
    DownloadUrl = Column(Text)
    ReadStateSynced = Column(Numeric, nullable=False, server_default=text("false"))
    TimesStartedReading = Column(Integer)
    TimeSpentReading = Column(Integer)
    LastTimeStartedReading = Column(Text)
    LastTimeFinishedReading = Column(Text)
    ApplicableSubscriptions = Column(Text)
    ExternalIds = Column(Text)
    PurchaseRevisionId = Column(Text)
    SeriesID = Column(Text)
    SeriesNumberFloat = Column(Float)
    AdobeLoanExpiration = Column(Text)
    HideFromHomePage = Column(Numeric)
    IsInternetArchive = Column(Boolean, nullable=False, server_default=text("FALSE"))
    titleKana = Column(Text)
    subtitleKana = Column(Text)
    seriesKana = Column(Text)
    attributionKana = Column(Text)
    publisherKana = Column(Text)


class ContentKey(Base):
    __tablename__ = 'content_keys'

    volumeId = Column(Text, primary_key=True, nullable=False, index=True)
    elementId = Column(Text, primary_key=True, nullable=False)
    elementKey = Column(Text)


class ContentSetting(Base):
    __tablename__ = 'content_settings'
    __table_args__ = (
        Index('content_settings_index', 'ContentID', 'ContentType'),
    )

    ContentID = Column(Text, primary_key=True, nullable=False)
    ContentType = Column(Integer, primary_key=True, nullable=False)
    DateModified = Column(Text, nullable=False)
    ReadingFontFamily = Column(Text)
    ReadingFontSize = Column(Integer)
    ReadingAlignment = Column(Text)
    ReadingLineHeight = Column(Float)
    ReadingLeftMargin = Column(Integer)
    ReadingRightMargin = Column(Integer)
    ReadingPublisherMode = Column(Integer)
    ActivityFacebookShare = Column(Numeric, server_default=text("TRUE"))
    RecentBookSearches = Column(Text)
    AuthorNotesShown = Column(Numeric, server_default=text("false"))
    LastAuthorNotesSyncTime = Column(Text)
    ZoomFactor = Column(Integer, server_default=text("1"))
    BTBFooterSection = Column(Text)
    SelectedDictionary = Column(Text)


class Event(Base):
    __tablename__ = 'Event'

    EventType = Column(Integer, primary_key=True, nullable=False)
    FirstOccurrence = Column(Text)
    LastOccurrence = Column(Text)
    EventCount = Column(Integer, server_default=text("0"))
    ContentID = Column(Text, primary_key=True, nullable=False)
    ExtraData = Column(LargeBinary)
    Checksum = Column(Text)


# Kobo Glo db contained this table
t_Images = Table(
    'Images', metadata,
    Column('ImageId', Text, nullable=False),
    Column('Type', Text, nullable=False),
    Column('Width', Integer, nullable=False),
    Column('Height', Integer, nullable=False)
)


class OverDriveCard(Base):
    __tablename__ = 'OverDriveCards'

    CardId = Column(Integer, primary_key=True)
    LibraryKey = Column(Text, nullable=False, index=True)
    BestLibraryKey = Column(Text, nullable=False)
    WebsiteId = Column(Integer, nullable=False)
    Name = Column(Text)
    LastModified = Column(Text)


class OverDriveCheckoutBook(Base):
    __tablename__ = 'OverDriveCheckoutBook'

    id = Column(Text, primary_key=True)
    title = Column(Text)
    libraryKey = Column(Text)
    cardId = Column(Text)


class OverDriveLibrary(Base):
    __tablename__ = 'OverDriveLibrary'

    Selected = Column(Numeric, nullable=False, server_default=text("false"))
    WebsiteId = Column(Integer, primary_key=True)
    LibraryKey = Column(Text)
    Name = Column(Text)


class Rating(Base):
    __tablename__ = 'ratings'

    ContentID = Column(Text, primary_key=True)
    Rating = Column(Integer)
    Review = Column(Text)
    DateModified = Column(Text, nullable=False)


class Review(Base):
    __tablename__ = 'Reviews'

    Id = Column(Text, primary_key=True)
    Header = Column(Text)
    Content = Column(Text)
    CreationDate = Column(Text)
    VolumeId = Column(Text, nullable=False)
    AuthorDisplayName = Column(Text)
    Sentiment = Column(Text)
    UserId = Column(Text)
    Likes = Column(Integer)
    Dislikes = Column(Integer)
    Rating = Column(Integer)
    SyncDate = Column(Text)
    Status = Column(Text)


class Rule(Base):
    __tablename__ = 'Rules'

    AchievementId = Column(Text)
    EventProperty = Column(Text)
    EventType = Column(Text)
    GoalValue = Column(Text, nullable=False)
    Id = Column(Text, primary_key=True)
    Operation = Column(Integer, nullable=False)
    ParentRuleId = Column(Text)
    ConjunctionType = Column(Integer)
    IsConjunction = Column(Boolean)
    Checksum = Column(Text)


class Shelf(Base):
    __tablename__ = 'Shelf'

    CreationDate = Column(Text, index=True)
    Id = Column(Text, primary_key=True, index=True)
    InternalName = Column(Text)
    LastModified = Column(Text)
    Name = Column(Text, index=True)
    Type = Column(Text)
    _IsDeleted = Column(Boolean)
    _IsVisible = Column(Boolean)
    _IsSynced = Column(Boolean)
    _SyncTime = Column(Text)
    LastAccessed = Column(Text)


class ShelfContent(Base):
    __tablename__ = 'ShelfContent'

    ShelfName = Column(Text, primary_key=True, nullable=False)
    ContentId = Column(Text, primary_key=True, nullable=False)
    DateModified = Column(Text, index=True)
    _IsDeleted = Column(Boolean)
    _IsSynced = Column(Boolean)


class ShortcoverPage(Base):
    __tablename__ = 'shortcover_page'

    shortcoverId = Column(Text, primary_key=True, nullable=False)
    PageNumber = Column(Integer, primary_key=True, nullable=False)
    FormattedPage = Column(Text)


class SyncQueue(Base):
    __tablename__ = 'SyncQueue'

    Date = Column(Text)
    VolumeId = Column(Text, primary_key=True)
    State = Column(Integer)


class Tab(Base):
    __tablename__ = 'Tab'

    tabId = Column(Text, primary_key=True)
    tabType = Column(Text)
    browseTabType = Column(Text)
    displayTitle = Column(Text)
    parentTabId = Column(Text)
    isDefault = Column(Boolean)
    maxSize = Column(Integer)
    totalResults = Column(Integer)
    updateFrequencyMin = Column(Integer)
    imageID = Column(Text)
    isLeaf = Column(Boolean)
    hasFeaturedLists = Column(Boolean)


class User(Base):
    __tablename__ = 'user'

    UserID = Column(Text, primary_key=True)
    UserKey = Column(Text, nullable=False)
    UserDisplayName = Column(Text)
    UserEmail = Column(Text)
    ___DeviceID = Column(Text)
    FacebookAuthToken = Column(Text)
    HasMadePurchase = Column(Numeric, server_default=text("FALSE"))
    IsOneStoreAccount = Column(Numeric, server_default=text("FALSE"))
    IsChildAccount = Column(Numeric, server_default=text("FALSE"))
    RefreshToken = Column(Text)
    AuthToken = Column(Text)
    AuthType = Column(Text)
    Loyalty = Column(LargeBinary)
    IsLibraryMigrated = Column(Numeric, nullable=False, server_default=text("true"))
    SyncContinuationToken = Column(Text)
    Subscription = Column(Integer, nullable=False, server_default=text("0"))
    LibrarySyncType = Column(Text)
    LibrarySyncTime = Column(Text)
    SyncTokenAppVersion = Column(Text)


class VolumeShortcover(Base):
    __tablename__ = 'volume_shortcovers'

    volumeId = Column(Text, primary_key=True, nullable=False)
    shortcoverId = Column(Text, primary_key=True, nullable=False)
    VolumeIndex = Column(Integer)


class VolumeTab(Base):
    __tablename__ = 'volume_tabs'

    volumeId = Column(Text, primary_key=True, nullable=False, index=True)
    tabId = Column(Text, primary_key=True, nullable=False, server_default=text("'abcdefff-ffff-ffff-ffff-fffffffffffd'"))


class WordList(Base):
    __tablename__ = 'WordList'

    Text = Column(Text, primary_key=True)
    VolumeId = Column(Text)
    DictSuffix = Column(Text)
    DateCreated = Column(Text)
