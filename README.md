sparchive
=========

sparchive is a simple, personal digital archival utility. It stores
your old files in a compact, versioned format that does not depend on
filesystem metadata (modification time, file name); this data is
stored within the archive file itself.

sparchive includes a "filer" program, which "files" your files and
directories into an archive directory.

sparchive is in *active development*. The file format may change without
notice!

Use cases
---------

You are writing a document, `foo.odt`. You have reached a point where
you want to archive a copy of this document. Type:

    sparchive file foo.odt

This will archive a copy foo.odt in a file called foo.odt.zip.rz,
stored in your archive dir (by default, `~/a`) in a simple year/month
directory tree, e.g. `2013/11/foo.odt.zip.rz`.

Now, after some time, you have made some changes to `foo.odt`, you can
archive a new version:

    sparchive file foo.odt

This will add a new version to your `2013/11/foo.odt.zip.rz` file.

You can do the same thing with directories:

    sparchive file dir/

Which will add a `2013/11/dir.zip.rz` file to your achive.

Because of sparchive's file format, similar data will be losslessly
compressed. So if, like me, you often end up with multiple directories
with similar files, you can safely file them away and sparchive will
store them in an efficent manner.

File format
-----------

sparchive files are standard ZIP files which should conform to the
following specification:

  http://www.idpf.org/epub/30/spec/epub30-ocf.html#physical-container-zip

(Not the whole spec, just that pertaining to ZIP files.)

sparchive files use the extended timestamp extra field to store last
modified time, and the external attributes to store permissions (but
not owners). Timestamps and permissions should be preserved for files
and directories.

